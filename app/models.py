# This is the database model

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# For the user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # Format for printing the object
    def __repr__(self):
        return '<User {}>'.format(self.username)  
    # Set password to hash 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # Check if password entered and hash matches 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class TestQuestion(db.Model):
    __tablename__ = 'TestQuestion'
    QuestionID = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.Text)
    QuestionText = db.Column(db.Text)
    Answerkey = db.Column(db.Text)
    

    def __repr__(self):
        return '<Question {},Answer {} >'.format(self.Question, self.Answerkey)


class UserAnswers(db.Model):
    UserTestID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey(User.id))
    Test_ID = db.Column(db.Integer)
    Question_No = db.Column(db.Integer)
    Question_ID = db.Column(db.Integer, db.ForeignKey(TestQuestion.QuestionID))
    User_Input = db.Column(db.String)

    def __repr__(self):
        return '<UserTestID:{}, UserID:{}, Test_ID:{},Question_No:{},Question_ID:{},User_Input:{}>'.format(self.UserTestID,self.User_ID,self.Test_ID,self.Question_No,self.Question_ID,self.User_Input)

class QuizAnswers(db.Model):
    QuizID = db.Column(db.Integer, primary_key=True)
    Module = db.Column(db.Text) #either Geometry, Indices, Simultaneous Equation
    QuizText = db.Column(db.Text) #question Identity
    QuizAnswer = db.Column(db.Float) #answer to get checked

    def check_answer(self, Answer):
        if self.QuizAnswer == Answer:
            return True
        else:
            return False

    def __repr__(self):
        return '<Module: {}, Question: {}, Answer: {} >'.format(self.Module,self.QuizText,self.QuizAnswer) 

class TransposingQuiz(db.Model): #for Transposing Equation
    QuizID = db.Column(db.Integer, primary_key=True)
    Module = db.Column(db.Text)
    Question = db.Column(db.Text) #question Identity
    Answer = db.Column(db.Text) #answer to get checked

    def __repr__(self):
        return '<Module: {}, Question: {}, Answer: {} >'.format(self.Module,self.Question,self.Answer) 

# Let applications to load users
@login.user_loader
def load_user(id):
    return User.query.get(int(id))    