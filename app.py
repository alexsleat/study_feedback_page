from flask import Flask, render_template, redirect, url_for, jsonify, request

app = Flask(__name__)

# list of questions.
# ## Each questions is a list: 0: UID, 1: title, 2: response options
QUESTIONS = [
    ["Q01", "radio_text", "how do you feel about the robot", ["hate", "dislike","neutral", "like", "love"]],
    ["Q02", "radio_text", "how was robots path", ["too cautious", "a bit cautious", "a bit aggressive", "too aggresive"]],
    ["Q03", "radio_img", "Emoji Response", ["1", "2","3", "4", "5"]]
]

USERID = -1
TRIALID = -1

### CSV Filename:
CSV_FILENAME = 'survey_results.csv'

def write_headers():

    ### Check for header line:
    first_line = ""
    with open(CSV_FILENAME) as f:
        first_line = f.readline().strip('\n')

    ### Write file headers
    h = "ParticipantID,TrialID,"
    for i in range(len(QUESTIONS)):
        current_q = QUESTIONS[i][0]
        h = h + current_q + " Response" + ("," if i<len(QUESTIONS)-1 else "")

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
    
    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")
        response_csv = ""
        for i in range(len(QUESTIONS)):
            current_q = QUESTIONS[i][0]
            content = request.form[current_q]

            response_csv = response_csv + "," + content 
            ### Responses from the webpage are handled here:
            print(USERID, TRIALID, response_csv)

        try:
            #return render_template('submittedandredirect.html')

            ### Save results to file:
            s = str(USERID) + "," + str(TRIALID) + response_csv 
            with open(CSV_FILENAME, 'a') as f:
                f.write(s + "\n")

            TRIALID = TRIALID + 1
            return render_template('bell.html', user=USERID, trial=TRIALID)
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    return render_template('index.html', user=USERID, trial=TRIALID, questions=QUESTIONS)



if __name__ == "__main__":
    write_headers()
    app.run(debug=True, host="0.0.0.0")