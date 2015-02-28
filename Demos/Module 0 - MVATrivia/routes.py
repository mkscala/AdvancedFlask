from flask import Flask, url_for, request, render_template;
from app import app;
import redis;

r = redis.StrictRedis(host='flaskmva.redis.cache.windows.net',port=6380,ssl=True,db=0, charset="utf-8", decode_responses=True, password='kxmLxHPfw5Xx8piaTlyv5VrPBBkKMoNTG6TNta+Pd5I=');

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

        r.set(title +':question', question)
        r.set(title +':answer',answer)
    
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "<h2>Invalid request</h2>";

# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')

        return render_template('AnswerQuestion.html', question = question);
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        answer = r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';