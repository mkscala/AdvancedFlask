import redis;

class Client(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='flaskmva.redis.cache.windows.net',port=6380,ssl=True,db=0, charset="utf-8", decode_responses=True, password='kxmLxHPfw5Xx8piaTlyv5VrPBBkKMoNTG6TNta+Pd5I=');
        return;

    def saveQuestion(self, title, question, answer):
        self.r.set(title +':question', question);
        self.r.set(title +':answer',answer);
        return;

    def getQuestion(self, title):
        return self.r.get(title + ':question');

    def getAnswer(self, title):
        return self.r.get(title + ':answer');