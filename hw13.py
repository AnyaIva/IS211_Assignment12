from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
from flask import flash, session
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('hw13.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            return redirect('/dashboard')
        else:
            print("Wrong username or password")
            return render_template('login.html')

    else:
        return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    students = conn.execute('SELECT student_id, first_name, last_name FROM students')
    quiz = conn.execute('SELECT quiz_id, subject, questions, quiz_date FROM quizzes')
    return render_template('dashboard.html', students=students, quiz=quiz)


@app.route('/showstudents')
def showstudents():
    conn = get_db_connection()
    students = conn.execute(f'SELECT student_id, first_name, last_name FROM Students where student_id = {id}')
    quiz = conn.execute(f'SELECT quiz_id, subject, questions, quiz_date FROM Quizzes where quiz_id = {id}')

    return render_template('showstudents.html', students=students, quiz=quiz)


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('addstudent.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        if not first_name:
            flash('Please enter first name')
        elif not last_name:
            flash('Please enter last name')
        else:
            conn = get_db_connection()
            conn.execute('insert into students (first_name, last_name) values (?, ?)',
                         [request.form['first_name'], request.form['last_name']])
            conn.commit()
            conn.close()
            flash('You added a new student')
            return redirect('/dashboard')


@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if request.method == 'GET':
        return render_template('addquizzes.html')
    elif request.method == 'POST':
        subject = request.form['subject']
        questions = request.form['questions']
        date = request.form['quiz_date']
        if not subject:
            flash('Please enter the subject')
        elif not questions:
            flash('Please enter the number of questions')
        elif not date:
            flash('Please enter the date of the quiz')
        else:
            conn = get_db_connection()
            conn.execute('insert into quizzes (subject, questions, quiz_date) '
                         'values (?, ?, ?)', [request.form['subject'],
                                              request.form['questions'],
                                              request.form['quiz_date']])
            conn.commit()
            conn.close()
            flash('You added a new quiz')
        return redirect('/dashboard')


@app.route('/results/add', methods=['GET', 'POST'])
def add_results():
    conn = get_db_connection()

    if request.method == 'GET':
        return render_template('addresult.html')
    elif request.method == 'POST':
        student_id = request.form['student_id']
        quiz_id = request.form['quiz_id']
        score = request.form['score']
        if not score:
            flash('Please enter the score')
        elif not student_id:
            flash('Please enter the student id')
        elif not quiz_id:
            flash('Please enter the quiz id')
        else:
            conn.execute("insert into quiz_results (student_id, quiz_id, score) values "
                         "(?, ?, ?)", (request.form['student_id'],
                                       request.form['quiz_id'], request.form['score']))
            conn.commit()
            conn.close()
            flash('You added a new result')
        return redirect('/dashboard')


if __name__ == "__main__":
    app.run()

  
