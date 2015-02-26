from flask import Flask, url_for, request, render_template;
from TriviaMVAApp import app;

from TriviaMVAApp.models.sqlclient import Client;

# server/
@app.route('/')
def hello():
    createLink = "<a href='" + url_for('create') + "'>Create a question</a>";
    return """<html>
                   <head>
                       <title>Hello, world!</title>
                    </head>
                    <body>
                       """ + createLink + """
                    </body>
               </html>""";

# server/create
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':

        return render_template('CreateQuestion.html');
    elif request.method == 'POST':

        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];

        client = Client();
        client.saveQuestion(title, question, answer);
    
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "<h2>Invalid request</h2>";

# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        client = Client();
        question = client.getQuestion(title);
        return render_template('AnswerQuestion.html', question = question);
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        client = Client();
        answer = client.getAnswer(title)

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';