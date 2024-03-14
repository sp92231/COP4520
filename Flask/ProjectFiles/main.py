from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('enternew.html')

@app.route('/addrec' , methods = ['POST' , 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            ag = request.form['age']
            pn = request.form['phone number']
            cv = request.form['Has COVID']
            srl = request.form['security role level']
            pas = request.form['password']

            with sql.connect("HospitalUsers.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO user (name, age, phone number, Has COVID, security role leve, password) "
                            "VALUES (?, ?, ?, ?, ?, ?)" , (nm, ag, pn, cv, srl, pas) )

                con.commit()
                msg = "Record successfully added"

        except:
            con.rollback()




@app.route('/list')
def list():
    return 'List Hospital App Users'

@app.route('/results')
def results():
    return 'Results'

if __name__ == '__main__':
    app.debug = True
    app.run()