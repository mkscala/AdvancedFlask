import pypyodbc;

class Client(object):
    def __init__(self):
        connectionString = 'Driver={SQL Server};Server=tcp:testpython.database.windows.net,1433;Database=test;Uid=test@testpython;Pwd=P@ssw0rd;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;';
        self.connection = pypyodbc.connect(connectionString);
        self.cursor = self.connection.cursor();
        return;

    def saveQuestion(self, title, question, answer):
        sql = "INSERT INTO Questions(QuestionName, Description, CorrectAnswer, CategoryID) VALUES (?,?,?,?)";
        values = [title, question, answer, 1];
        self.cursor.execute(sql, values);
        self.connection.commit();
        self.connection.close();
        return;

    def getQuestion(self, title):
        sql = "SELECT Description FROM Questions WHERE QuestionName = ?";
        values = [title];
        self.cursor.execute(sql, values);
        results = self.cursor.fetchone();
        question = results[0];
        self.connection.close();
        return question;

    def getAnswer(self, title):
        sql = "SELECT CorrectAnswer FROM Questions WHERE QuestionName = ?";
        values = [title];
        self.cursor.execute(sql, values);
        results = self.cursor.fetchone();
        correctAnswer = results[0];
        self.connection.close();
        return correctAnswer;    