from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('enternew.html')


@app.route('/addrec' , methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':

        nm = request.form['Name']
        ag = request.form['Age']
        pn = request.form['PhoneNumber']
        cv = request.form.get('COVID', 0)
        srl = request.form['SecurityLevel']
        pwd = request.form['Password']

        error_msgs = []

        if (len(nm.strip()) == 0):
            error_msgs.append("Can not add record...Name is required.")
        elif not ag.isdigit():
            error_msgs.append("Can not add record...Age must be a valid number.")
        else:
            ag = int(request.form['Age'])
            if(ag < 1 or ag > 120):
                error_msgs.append("Can not add record...Age must be between 1 and 120.")
        if (len(pn.strip()) == 0):
            error_msgs.append("Can not add record...Phone Number is required.")
        if not srl.isdigit():
            error_msgs.append("Can not add record...Security Role Level must be between 1 and 3.")
        else:
            srl = int(srl)
            if srl < 1 or srl > 3:
                error_msgs.append("Can not add record...Security Role Level must be between 1 and 3.")
        if (len(pwd.strip()) == 0):
            error_msgs.append("Can not add record...Password is required.")

        if error_msgs:
            return render_template("result.html", msg=error_msgs)

        else:
            try:
                with (sql.connect('HospitalUsers.db') as con):
                    cur = con.cursor()

                    cur.execute(
                        "INSERT INTO HospitalUser (Name, Age, PhoneNumber, COVID, SecurityLevel, Password) "
                        "VALUES (?, ?, ?, ?, ?, ?)", (nm, ag, pn, cv, srl, pwd))

                    con.commit()
                    error_msgs.append("Record successfully added.")

            except:
                con.rollback()
                error_msgs.append("Error in insertion operation.")
            finally:
                return render_template("result.html", msg=error_msgs)
                con.close()


@app.route('/list')
def list():
    con = sql.connect('HospitalUsers.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from HospitalUser")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

@app.route('/results')
def results():
    return 'Results'

if __name__ == '__main__':
    app.debug = True
    app.run()