from flask import Flask, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from questions import QUESTIONS

app = Flask(__name__)

USERID = -1
TRIALID = -1
TRIAL_COUNTER = 0

### CSV Filename:
CSV_FILENAME = 'survey_results.csv'

def write_headers():

    ### Check for header line:
    first_line = ""
    with open(CSV_FILENAME) as f:
        first_line = f.readline().strip('\n')

    ### Write file headers
    h = "Time,ParticipantID,TrialID,"
    for k, v in QUESTIONS.items():
        for i in range(len(v)):
            current_q = v[i][0]
            h = h + current_q + " Response" + ", "#("," if i<len(v)-1 else "")

    if(h == first_line):
        print("Header exists")
    else:
        with open(CSV_FILENAME, 'a') as f:
            f.write(h + "\n")

######################
# Routes
######################

## Home ####################
@app.route('/', methods=['POST', 'GET'])
def home():

    global USERID
    global TRIALID

    if request.method == 'POST':
        USERID = int(request.form['paricipantID'])
        TRIALID = int(request.form['trialID'])
        
        print(USERID, TRIALID)

        return render_template('bell.html', user=USERID, trial=TRIALID)

    return render_template('start.html')

## Bell ####################
@app.route('/bell')
def bell():

    global USERID
    global TRIALID

    return render_template('bell.html', user=USERID, trial=TRIALID)

## Questions Page ####################
@app.route('/questions', methods=['POST', 'GET'])
def showQuestions():

    global USERID
    global TRIALID
    global TRIAL_COUNTER
    
    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")
        response_csv = ""
        
        for i in range(len(QUESTIONS[TRIAL_COUNTER])):
            current_q = QUESTIONS[TRIAL_COUNTER][i][0]
            content = request.form[current_q]

            response_csv = response_csv + "," + content 
            ### Responses from the webpage are handled here:
            print(USERID, TRIALID, response_csv)

        try:
            ### Save results to file:
            now = datetime.now()
            s = now.strftime("%H:%M:%S:%f") + "," + str(USERID) + "," + str(TRIALID) + response_csv 
            with open(CSV_FILENAME, 'a') as f:
                f.write(s + "\n")

            TRIALID = TRIALID + 1
            return render_template('bell.html', user=USERID, trial=TRIALID)
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    TRIAL_COUNTER = TRIAL_COUNTER + 1
    if(TRIAL_COUNTER <= len(QUESTIONS.items())):
        return render_template('index.html', user=USERID, trial=TRIALID, questions=QUESTIONS[TRIAL_COUNTER])
    else:
        return render_template('fin.html')



if __name__ == "__main__":
    write_headers()
    app.run(debug=True, host="0.0.0.0")