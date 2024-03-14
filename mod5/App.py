"""

Name:Shanie Portal
Date: 10/03/2023
Assignment: Module 5: Role Based Access Control
Due Date: 10/01/2023
About this project: Adding Role Based Access Controls to flask website.
Assumptions:
All work below was performed by: Shanie Portal

"""
from flask import Flask, render_template, request, session, flash
import sqlite3 as sql
import os

#Create Flask instance.
app = Flask(__name__)

#Route to home page.
@app.route('/')
def home():  # home page
    #Check if user is not logged in.
    if not session.get('logged_in'):
        #Redirect to login page.
        return render_template('login.html')
    else:
        #Render home page with user's name.
        return render_template('home.html', name=session['name'])

#Route to enter new user data.
@app.route('/enternew')
def enternew():
    #Check if the user is not logged in.
    if not session.get('logged_in'):
        #Redirect to login page.
        return render_template('login.html')
    #Check if user is an admin.
    elif session.get('admin') == True:
        #Render the enternew form.
        return render_template('enternew.html')  # Render the form for adding a new user


#Route for adding records.
@app.route('/addrec' , methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        #Retrieve user data from form.
        nm = request.form['Name']
        ag = request.form['Age']
        pn = request.form['PhoneNumber']
        cv = request.form.get('COVID', 0)
        srl = request.form['SecurityLevel']
        pwd = request.form['Password']

        error_msgs = []

        #Validate user input data.
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

        #If there are errors, display them.
        if error_msgs:
            return render_template("result.html", msg=error_msgs)

        else:
            try:
                #Connect to database.
                with (sql.connect('HospitalUsers.db') as con):
                    cur = con.cursor()

                    #Insert user data into database.
                    cur.execute(
                        "INSERT INTO HospitalUser (Name, Age, PhoneNumber, COVID, SecurityLevel, Password) "
                        "VALUES (?, ?, ?, ?, ?, ?)", (nm, ag, pn, cv, srl, pwd))

                    #Commit database changes.
                    con.commit()
                    error_msgs.append("Record successfully added.")

            #Rollback data in event of an error.
            except:
                con.rollback()
                error_msgs.append("Error in insertion operation.")
            finally:
                return render_template("result.html", msg=error_msgs)
                #Close database connection.
                con.close()

#Route for listing records.
@app.route('/list')
def list():
    #Connect to database.
    con = sql.connect('HospitalUsers.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from HospitalUser")

    #Fetch all rows from database.
    rows = cur.fetchall()
    #Render the list.
    return render_template("list.html", rows=rows)

#Route for login.
@app.route('/login', methods=['POST'])
def do_admin_login():
    try:
        #Retrieve username and password from form.
        nm = request.form['Username']
        pwd = request.form['Password']

        #Connect to database.
        with sql.connect('HospitalUsers.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()

            #Query the database for credentials.
            sql_select_query = """select * from HospitalUser where Name = ? and Password = ?"""
            cur.execute(sql_select_query, (nm, pwd))

            row = cur.fetchone();
            if row is not None:
                #Set variables for successful login.
                session['logged_in'] = True
                session['name'] = nm
                session['SecurityLevel'] = int(row['SecurityLevel'])
                session['admin'] = (session['SecurityLevel'] >= 2)  # Check if user is admin
            else:
                #Display an error message for invalid credentials.
                session['logged_in'] = False
                flash('Invalid username and/or password!')
    except:
        #Display error message.
        con.rollback()
        flash("Error in insert operation.")
    finally:
        #Close connection to database.
        con.close()
    #Redirect to home.
    return home()

#Route to display user information.
@app.route('/userInfo')
def displayInfo():
    if not session.get('logged_in'):
        #Check if the user is not logged in and redirect to the login page.
        return render_template('login.html')
    else:
        username = session.get('name')

        #Connect to database.
        con = sql.connect('HospitalUsers.db')
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute(
            "SELECT Name, Age, PhoneNumber, COVID, SecurityLevel, Password FROM HospitalUser WHERE Name=?",
            (username,))

        #Fetch user information.
        rows = cur.fetchall()

        # Return the user information.
        return render_template('userInfo.html', rows=rows)

#Route for logout.
@app.route("/logout")
def logout():
    #Clear session variables to logout.
    session['logged_in'] = False
    session['admin'] = False
    session['name'] = ""

    #Redirect user home.
    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)