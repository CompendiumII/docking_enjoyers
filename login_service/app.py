from flask import Flask, render_template, request, redirect, session, url_for
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'your_secret_key'

AUTH_SERVICE_URL = 'http://auth_service:5000/login'

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = 'password1'
app.config['MYSQL_DB'] = 'analytics_data'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/result')
def result():
    if 'username' in session:
        return redirect('http://localhost:5006')
    
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    data = {'username': username, 'password': password}
    response = requests.post(AUTH_SERVICE_URL, json=data)

    if response.status_code == 200:
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('login.html', error='Authentication failed. Please try again.')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/input', methods=['GET', 'POST'])
def input():
    if 'username' in session:
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_id = request.form['student_id']
            course = request.form['course']
            grade = request.form['grade']
            
            dbcursor = mysql.connection.cursor()
            dbcursor.execute("INSERT INTO student_grades (student_name, student_id, course, grade) VALUES (%s, %s, %s, %s)",
                        (student_name, student_id, course, grade))
            dbcursor.execute("select * from student_grades")
            results = dbcursor.fetchall()
            for row in results:
                print(row)
            mysql.connection.commit()
            dbcursor.close()
            return redirect('/input')

        return render_template('input.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)