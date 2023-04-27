# Flask server with forms for feedback

## Requirements:
pip3 install flask gunicorn

## Run:
python3 app.py

## Update code:
git pull

# App overview:

### app.py
This is the main logic of the program, which will assign webpages to html files to be rendered, redirect accordingly on form completion of the page, or generate the questions to show on other pages. It also deals with storing the data and in csv files.

### start.html

app.py function for the file:
    @app.route('/', methods=['POST', 'GET'])
    def home():

This is the starting page of the questionaire, designed for the experimenter to assign an ID and starting trial for the user.

It's a good example of showing the logic of most of the program, where app.py (function above) deals with assigning it a url for the server (in this case '/'). 

The if statement deals with the data being returned from the webpage to the server on "submit" from the form. This then stores the data in the json variable, and redirects to another page on success or failure.

The return below the if (which will be called, on a regular visit, before submission of the form) renders the start.html page.

Most of the other functions follow this same logic, meaning you can make simple questionaires, or ones unlikely to change, or that don't need to be randomized this way. Create a new html page to render, create a function and assign it a url, and fit it into the logic by having another function direct you there.

### questions.py & index.html

app.py function for the files:
    ## Questions Page ####################
    @app.route('/questions', methods=['POST', 'GET'])
    def showQuestions():

This function works a little differently. It uses the questions from the python file to dynamically generate the order and render the template. This gives a good example of passing data from the server to a html page being rendered:

    # in app.py
    return render_template('index.html', user=USERID, trial=TRIALID, questions=QUESTIONS_TO_DISPLAY)

Which is handled by the html file in the following way:

    # in index.html
    {% for message in questions %}
        <div class="{{ message[1] }}">

The questions in the html file, relates to the data from app.py's render_template.