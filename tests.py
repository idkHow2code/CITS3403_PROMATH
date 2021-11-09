from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, QuizAnswers

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('11111'))
        self.assertTrue(u.check_password('cat'))

    def test_login_Required_Geometry(self):
        tester = app.test_client(self)
        response = tester.get('/geometry', content_type='html/text')
        self.assertFalse(b'Please login' in response.data)

    def test_login_Required_Indices(self):
        tester = app.test_client(self)
        response = tester.get('/indices', content_type='html/text')
        self.assertFalse(b'Please login' in response.data)

    def test_login_Required_Simultaneous(self):
        tester = app.test_client(self)
        response = tester.get('/simultaneous_equations', content_type='html/text')
        self.assertFalse(b'Please login' in response.data)

    def test_login_Required_Transposing(self):
        tester = app.test_client(self)
        response = tester.get('/transposing_equations', content_type='html/text')
        self.assertFalse(b'Please login' in response.data)

class QuizModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_indices_quiz(self):
        indices_q1 = QuizAnswers(Module='Indices', QuizText='3^0', QuizAnswer=1)
        indices_q2 = QuizAnswers(Module='Indices', QuizText='100^0', QuizAnswer=1)
        db.session.add(indices_q1)
        db.session.add(indices_q2)
        db.session.commit()
        self.assertFalse(indices_q1.check_answer(2))
        self.assertTrue(indices_q1.check_answer(1))
if __name__ == '__main__':
    unittest.main(verbosity=2)