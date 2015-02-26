from flask import Flask, url_for, request, render_template;
from TriviaMVAApp import app;
import redis;

from TriviaMVAApp.models.redisclient import RedisClient;
redisClient = RedisClient();

# server/
@app.route('/')
def hello():

    #alternate ways to connect to redis, each command is equivalent
    #r = redis.StrictRedis();
    #r = redis.StrictRedis('localhost',6379,0);


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
        # send the user the form
        return render_template('CreateQuestion.html');
    elif request.method == 'POST':
        # read form data and save it
        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];

        redisClient.saveQuestion(title, question, answer);
    
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "<h2>Invalid request</h2>";

# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = redisClient.getQuestion(title);
      
        return render_template('AnswerQuestion.html', question = question);
    elif request.method == 'POST':
        # User has attempted answer. Check if they're correct
        submittedAnswer = request.form['submittedAnswer'];

        # Read answer from data store
        # Susan - please add code here
        answer = redisClient.getAnswer(title+':answer')

        if submittedAnswer == answer:
            return "Correct!"
            #return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';