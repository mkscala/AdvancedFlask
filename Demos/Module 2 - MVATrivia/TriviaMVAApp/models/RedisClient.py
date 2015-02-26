import redis;

class RedisClient(object):
    r = redis.StrictRedis(host='flaskmva.redis.cache.windows.net',port=6380,ssl=True,db=0, charset="utf-8", decode_responses=True, password='kxmLxHPfw5Xx8piaTlyv5VrPBBkKMoNTG6TNta+Pd5I=');

    def __init__(self):
        # Nothing to initialize
        return;

    def saveQuestion(self, title, question, answer):
        r.set(title +':question', question);
        r.set(title +':answer',answer);
        return;

    def getQuestion(self, title):
        return r.get(title + ':question');

    def getAnswer(self, title):
        return r.get(title + ':question');