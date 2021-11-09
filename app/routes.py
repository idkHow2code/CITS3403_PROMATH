from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, ChangeUsernameForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, QuizAnswers, TestQuestion, UserAnswers, TransposingQuiz
from flask import request
from werkzeug.urls import url_parse
from sqlalchemy.sql.expression import func
from sqlalchemy import desc

#QuestionList = request.form["QuestionList"],QuestionList=QuestionList
@app.route('/')
@app.route('/homepage')
#@login_required # force login before viewing other pages
def homepage():
    return render_template('homepage.html')

@app.route('/transposing_equations/<username>')
@login_required
def transposing_equations(username):
    quizQuestions = []
    for quiz in TransposingQuiz.query.all():
        if quiz.Module == 'Transposing':
            Question = {
                'Question' : quiz.Question,
                'Answer' : quiz.Answer
            }
            quizQuestions.append(Question)

    user = User.query.filter_by(username=username).first_or_404()
    return render_template('Transposing_Equations.html',user=user, quiz=quizQuestions)

@app.route('/indices/<username>', methods=['GET', 'POST'])
@login_required
def indices(username):
    quizQuestions = []
    for quiz in QuizAnswers.query.all():
        if quiz.Module == 'Indices':
            Question = {
                'Question' : quiz.QuizText,
                'Answer' : quiz.QuizAnswer
            }
            quizQuestions.append(Question)

    user = User.query.filter_by(username=username).first_or_404()
    return render_template('indices.html',user=user, quiz=quizQuestions)

@app.route('/simultaneous_equations/<username>', methods=['GET', 'POST'])
@login_required
def simultaneous_equations(username):
    quizQuestions = []
    for quiz in QuizAnswers.query.all():
        if quiz.Module == 'Simultaneous':
            Question = {
                'Question' : quiz.QuizText,
                'Answer' : quiz.QuizAnswer
            }
            quizQuestions.append(Question)

    user = User.query.filter_by(username=username).first_or_404()
    return render_template('simultaneous_equations.html',user=user, quiz=quizQuestions)

@app.route('/geometry/<username>', methods=['GET', 'POST'])
@login_required
def geometry(username):
    quizQuestions = []
    for quiz in QuizAnswers.query.all():
        if quiz.Module == 'Geometry':
            Question = {
                'Question' : quiz.QuizText,
                'Answer' : quiz.QuizAnswer
            }
            quizQuestions.append(Question)
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('Geometry.html',user=user, quiz=quizQuestions)

@app.route('/progress/<username>')
@login_required
def progress(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('basics_progress.html',user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('homepage')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/change_username', methods=['GET', 'POST'])
def change_username():
    form = ChangeUsernameForm(current_user.username)
    if form.validate_on_submit():
            current_user.username = form.username.data
            db.session.commit()
            flash('Your changes have been saved.') 
            return redirect(url_for('homepage'))
    elif request.method == 'GET':
        form.username.data = current_user.username
       
    return render_template('change_username.html', title='Change Username', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('after_register', username=user.username))
    return render_template('register.html', title='Register', form=form)

@app.route('/afterRegister/<username>')
def after_register(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('afterRegister.html',user=user)

@app.route('/test/<username>')
@login_required
def test(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('basicTest.html',user=user)


@app.route('/test_active/<username>', methods=['GET', 'POST'])
def test_active(username):
    if request.method == "POST":
        user = User.query.filter_by(username=username).first_or_404()
        ExamQuestions = []
        for question in TestQuestion.query.all():
            Question = {
                'Question' : question.Question,
                'Answer' : question.Answerkey
            }
            ExamQuestions.append(Question)
        answer1 = request.form["Answer1"]
        answer2 = request.form["Answer2"]
        answer3 = request.form["Answer3"]
        answer4 = request.form["Answer4"]
        answer5 = request.form["Answer5"]
        Question1 = request.form["Question1"]
        Question2 = request.form["Question2"]
        Question3 = request.form["Question3"]
        Question4 = request.form["Question4"]
        Question5 = request.form["Question5"]
        return render_template('testResult.html',answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,Question1=Question1,Question2=Question2,Question3=Question3,Question4=Question4,Question5=Question5,TestQuestions=ExamQuestions,user=user)
    else:  #'GET' method
        user = User.query.filter_by(username=username).first_or_404()
        testQuestions = []
        randomTestQuestions = TestQuestion.query.order_by(func.random()).limit(5)

        for question in randomTestQuestions:
            Quest = {
                'Question' : question.Question,
                'QuestionText' : question.QuestionText
            }
            testQuestions.append(Quest)

        image = "/static/ExamQuestions/Transposing_Q2.png"

        return render_template('test.html', quiz=testQuestions, image=image)

# To log out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))