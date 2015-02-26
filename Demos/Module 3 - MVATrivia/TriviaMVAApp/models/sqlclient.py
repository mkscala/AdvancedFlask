import pypyodbc;

class Client(object):
    __connectionString = 'Driver={SQL Server};Server=tcp:123fgt7.database.windows.net,1433;Database=MyAzureDatabase;Uid=susanibach@123fgt7;Pwd=P@ssw0rd;Encrypt=yes';
       
    def __init__(self):
        self.connection = pypyodbc.connect(__connectionString);
        self.cursor = connection.cursor();
        return;

    def saveQuestion(self, title, question, answer):
        sql = "INSERT INTO Questions(QuestionName, Description, CorrectAnswer, CategoryID) VALUES (?,?,?,?)";
        values = ['Test', 'This is a test', 'Test', 1];
        self.cursor.execute(sql, values);
        self.connection.commit();
        self.connection.close();
        return;

    def getQuestion(self, title):
        sql = "SELECT Description FROM Questions WHERE QuestionName = ?";
        values = ['Test'];
        self.cursor.execute(sql, values);
        self.connection.commit();
        self.connection.close();
        return;
    def getAnswer(self, title):
        return r.get(title + ':question');

    