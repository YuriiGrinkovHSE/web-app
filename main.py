from flask import Flask, render_template, url_for, request, flash, redirect, g
import sqlite3
import os
from FDataBase import FDataBase
DATABASE = 'C:/Users/1/users1.db'
DEBUG = True
SECRET_KEY='efjwofjwijfwoijfoi'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'users1.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('mySQLfile.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link.db'):
        g.link_db=connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link.db'):
        g.link_db.close()

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')


@app.route('/')
def index():
    if request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'обществознание':
        return redirect(url_for('rusmatsoc'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'английский язык':
        return redirect(url_for('rusmatsoc'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'физика':
        return redirect(url_for('rusmatsoc'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'информатика':
        return redirect(url_for('rusmatsoc'))
    elif request.method == 'POST' and request.form['first_item'] != '' and request.form[
        'second_item'] != '' and request.form['third_item'] != '':
        return redirect('page404.html')
    else:
        return render_template('index.html')






@app.route('/index', methods=['POST', 'GET'])
def main():
    if request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'обществознание':
            return redirect(url_for('rusmatsoc'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'английский язык':
            return redirect(url_for('rusmateng'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'физика':
            return redirect(url_for('rusmatphy'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'математика' and request.form['third_item'] == 'информатика':
            return redirect(url_for('rusmatinf'))
    elif request.method == 'POST' and request.form['first_item'] == 'русский язык' and request.form[
        'second_item'] == 'обществознание' and request.form['third_item'] == 'история':
            return redirect(url_for('russochis'))
    #... Продолжение условных операторов
    elif request.method == 'POST' and request.form['first_item'] != '' and request.form[
        'second_item'] != '' and request.form['third_item'] != '':
        return redirect('page404.html')
    return render_template('index.html')

@app.route('/index.html/rusmatphy')
def rusmatphy():
    return render_template('rusmatphy.html')

@app.route('/index.html/rusmatinf')
def rusmatinf():
    return render_template('rusmatinf.html')

@app.route('/index.html/rusmatsoc')
def rusmatsoc():
    return render_template('rusmatsoc.html')

@app.route('/index.html/russochis')
def russochis():
    return render_template('russochis.html')

@app.route('/index.html/rusmateng')
def rusmateng():
    return render_template('rusmateng.html')


@app.route('/interactive.html')
def interestingLinks():
    return render_template('interactive.html')


@app.route('/feedback.html', methods=['POST', 'GET'])
def feedback():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if (len(request.form["contact_name"]) > 1) and (len(request.form['contact_surname']) > 1) and (
                len(request.form['contact_message']) > 1):
            res = dbase.getFeedback(request.form['contact_name'], request.form['contact_surname'], request.form['contact_message'])
            if not res:
                flash('Сообщение не отправлено. Должно быть введено как минимум два символа в каждой форме.',
                      category='error')
            else:
                flash('Сообщение отправлено', category='success')

        print(request.form)
    return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug=True)  # host='0.0.0.0'
