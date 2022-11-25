from flask import Flask, render_template, redirect, url_for, jsonify, request

app = Flask(__name__)

# list of questions.
# ## Each questions is a list: 0: UID, 1: title, 2: response options
QUESTIONS = [
    ["Q01", "radio_text", "how do you feel about the robot", ["hate", "dislike","neutral", "like", "love"]],
    ["Q02", "radio_text", "how was robots path", ["too cautious", "a bit cautious", "a bit aggressive", "too aggresive"]],
    ["Q03", "radio_img", "Emoji Response", ["1", "2","3", "4", "5"]]
]

######################
# Routes
######################

## Home ####################
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))

    return render_template('start.html')
   

## Questions Page ####################
@app.route('/questions', methods=['POST', 'GET'])
def showQuestions():
    data = {}

    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")
        response = {}
        for i in range(len(QUESTIONS)):
            current_q = QUESTIONS[i][0]
            content = request.form[current_q]

            ### Responses from the webpage are handled here:
            print(current_q, content)

        try:
            #return jsonify({'page': 'questions', 'success': True, 'responses' : data})
            return render_template('submittedandredirect.html')
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    return render_template('index.html', questions=QUESTIONS)



if __name__ == "__main__":
    app.run(debug=True)