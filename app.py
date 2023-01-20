from flask import Flask, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from questions import QUESTIONS
import csv

app = Flask(__name__)

USERID = -1
TRIALID = ""
TRIAL_COUNTER = 0
TRIAL_TYPE = "vr"
TRIALS_COMPLETED = {"vr": False, "screen": False}

### CSV Filename:
CSV_FILENAME = 'survey_results.csv'
JSON_DATA = {}

def write_headers():

    ### Check for header line:
    first_line = ""
    with open(CSV_FILENAME) as f:
        first_line = f.readline().strip('\n')

    ### Write file headers
    JSON_DATA["ParticipantID"] = ""
    JSON_DATA["TrialID"] = ""

    h = "Time,ParticipantID,TrialID,"
    for v in QUESTIONS:
        current_q = v[0]
        h = h + current_q + ", " #+ ("," if i<len(v)-1 else "")

        JSON_DATA[current_q] = ""

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
    global JSON_DATA

    if request.method == 'POST':
        USERID = int(request.form['paricipantID'])
        TRIALID = request.form['trialID']
        
        print(USERID, TRIALID)

        JSON_DATA["ParticipantID"] = USERID
        JSON_DATA["TrialID"] = TRIALID

        #return render_template('consent.html', user=USERID, trial=TRIALID)
        return redirect('/consent')

    return render_template('start.html')

## final_opinions ####################
@app.route('/final_opinions', methods=['POST', 'GET'])
def final_opinions():

    global USERID
    global TRIALID

    if request.method == 'POST':
                
        print(request.form)
        for v in request.form:
            JSON_DATA[v] = request.form[v]
        
        print("FINAL RESPONSE JSON: ", JSON_DATA)

        return redirect('/fin')

    return render_template('final_opinions.html', user=USERID, trial=TRIALID)


## consent ####################
@app.route('/consent', methods=['POST', 'GET'])
def consent():

    global USERID
    global TRIALID
    global JSON_DATA

    if request.method == 'POST':
     
        print(request.form)
        for v in request.form:
            JSON_DATA[v] = request.form[v]

        if(JSON_DATA["consent_1"] == "No"):
            return redirect('/fin')
        return redirect('/demographics')

    return render_template('consent.html', user=USERID, trial=TRIALID)

## demographics ##############
@app.route('/demographics', methods=['POST', 'GET'])
def demographics():

    global USERID
    global TRIALID
    global JSON_DATA

    if request.method == 'POST':
     
        print(request.form)
        for v in request.form:
            JSON_DATA[v] = request.form[v]

        return redirect('/questions')

    return render_template('demographics.html', user=USERID, trial=TRIALID)

## Bell ####################
@app.route('/bell', methods=['POST', 'GET'])
def bell():

    global USERID
    global TRIALID

    return render_template('bell.html', user=USERID, trial=TRIALID)

## Fin ####################
@app.route('/fin', methods=['POST', 'GET'])
def fin():

    global USERID
    global TRIALID

    with open(CSV_FILENAME, 'a') as f:
        # f.write(s + "\n")
        w = csv.DictWriter(f, JSON_DATA.keys())
        w.writeheader()
        w.writerow(JSON_DATA)

    return render_template('fin.html', user=USERID, trial=TRIALID)

## Questions Page ####################
@app.route('/questions', methods=['POST', 'GET'])
def showQuestions():

    global USERID
    global TRIALID
    
    # Calculate which questions to use:
    print(USERID, TRIALID)
    QUESTIONS_TO_DISPLAY=return_questions_for_condition(QUESTIONS, TRIALID)

    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")
        # response_csv = ""
        print(request.form)
        
        for i in range(len(QUESTIONS_TO_DISPLAY)):

            try:
                current_q = QUESTIONS_TO_DISPLAY[i][0]
                content = request.form[current_q]

                JSON_DATA[current_q] = content

                # response_csv = response_csv + "," + content 
                # ### Responses from the webpage are handled here:
            except Exception as exc:
                current_q = QUESTIONS_TO_DISPLAY[i][0]
                JSON_DATA[current_q] = -1
                print("no data for: ", current_q)
        
        print("JSON: ", JSON_DATA)
        # print("CSV: ", USERID, TRIALID, response_csv)

        try:
            ### Save results to file:
            now = datetime.now()
            # s = now.strftime("%H:%M:%S:%f") + "," + str(USERID) + "," + str(TRIALID) + response_csv 
            # with open(CSV_FILENAME, 'a') as f:
            #     f.write(s + "\n")

            if TRIALID == "vr":
                TRIALS_COMPLETED["vr"] = True
                TRIALID = "screen"
            else:
                TRIALS_COMPLETED["screen"] = True
                TRIALID = "vr"

            if(TRIALS_COMPLETED["vr"] == True and TRIALS_COMPLETED["screen"] == True):
                return redirect('/final_opinions')

            return render_template('bell.html', user=USERID, trial=TRIALID)
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    return render_template('index.html', user=USERID, trial=TRIALID, questions=QUESTIONS_TO_DISPLAY)


def return_questions_for_condition(questions, condition):

    questions_to_display = []
    
    for q in questions:
        if "vr" in condition and "_VR" in q[0]:
            questions_to_display.append(q)
        elif "screen" in condition and "_S" in q[0]:
            questions_to_display.append(q)

    print("Questions calculatd", questions_to_display)
    return questions_to_display

if __name__ == "__main__":
    # write_headers()
    app.run(debug=True, host="0.0.0.0", port=1231)
