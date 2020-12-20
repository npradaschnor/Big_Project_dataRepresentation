#!flask/bin/python
from flask import Flask, url_for, jsonify, session, request, abort, make_response, render_template, redirect, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg
from PatientDao import patientDao 
from DoctorDao import doctorDao

#Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')

app.secret_key = 'k9WydtaAVn9E2HmHy0T3VvcRHJzdDZQp'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'datarepresentation'

mysql = MySQL(app)

#Need to login
@app.route('/')
def root():
    if not 'username' in session:
        return redirect(url_for('login'))

#####################Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT username,password FROM users WHERE username=%s", [username])
        user = cur.fetchone()
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = user['username']
            return render_template('home.html', username=username)
        
        else:
            flash('Invalid Username or Password !!')
            return render_template('login.html')
    else:
        return render_template('login.html')

######################### Logout
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


#/home route renders home template
@app.route('/home')
def home():
    pagetitle = "HomePage"

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('home.html', mytitle=pagetitle)

######################### Patients table

# /patientdata route renders patientviewer template
@app.route('/patientdata')

def patientData():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('patientviewer.html')
    
    

# /patients get all the patients records in JSON
@app.route('/patients')

def getAll():

    if not 'username' in session:
        abort(401)

    return jsonify(patientDao.getAll())
    #return jsonify({'patients':patients})

#curl "http://127.0.0.1:5000/patients"
# curl -i "http://localhost:5000/patients"

# /patient/<id> get the record of a specific patient (by id)
@app.route('/patients/<id>')

def findById(id):
    if not 'username' in session:
        abort(401)

    return jsonify(patientDao.findById(id))

#curl "http://127.0.0.1:5000/patients/F4386D"

@app.route('/patients', methods=['POST'])

def create():

    if not request.json:
        abort(400) #check that the request has JSON data (if not returns a 400 error)

    patient={
        "id": request.json["id"],
        "firstName": request.json["firstName"],
        "lastName":request.json["lastName"],
        "reasonForVisiting":request.json["reasonForVisiting"]
    } #read the request object and create a new patient

    patientAdd = patientDao.create(patient)
    
    return jsonify(patientAdd)

# curl -i -H "Content-Type:application/json" -X POST -d '{"id":"W9146A","firstName":"Fiona","lastName":"OBrien","reasonForVisiting":"OBES"}' http://127.0.0.1:5000/patients

#Windows:
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"W9146A\",\"firstName\":\"Fiona\",\"lastName\":\"OBrien\",\"reasonForVisiting\":\"OBES\"}" http://127.0.0.1:5000/patients

#This is a put and it takes in the id from the url
@app.route('/patients/<id>', methods =['PUT'])

def update(id):
    foundPatient=patientDao.findById(id)

    #print (foundPatient)

    if foundPatient == {}:
        return jsonify({}), 404

    if not request.json:
        abort(400)

    currentPatient = foundPatient

    if 'id' in request.json:
        currentPatient['id'] = request.json['id']
    if 'firstName' in request.json:
        currentPatient['firstName'] = request.json['firstName']
    if 'lastName' in request.json:
        currentPatient['lastName'] = request.json['lastName']
    if 'reasonForVisiting' in request.json:
        currentPatient['reasonForVisiting'] = request.json['reasonForVisiting']

    patientDao.update(currentPatient)

    return jsonify(currentPatient)

#curl -i -H "Content-Type:application/json" -X PUT -d '{"lastName":"OReilly"}' http://127.0.0.1:5000/patients/R3650A

#Windows:
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"lastName\":\"OReilly\"}" http://127.0.0.1:5000/patients/R3650A

@app.route('/patients/<id>', methods =['DELETE'])

def delete(id):
    patientDao.delete(id)
    return  jsonify( {'Done':True })

################### Doctors table

# /doctordata route renders doctorviewer template
@app.route('/doctordata')
def doctorData():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('doctorviewer.html')

# /patients get all the doctors records in JSON


@app.route('/doctors')
def getAllDoc():

    if not 'username' in session:
        abort(401)

    return jsonify(doctorDao.getAllDoc())
    #return jsonify({'doctors':doctors})

#curl "http://127.0.0.1:5000/doctors"
# curl -i "http://localhost:5000/doctors"

# /patient/<id> get the record of a specific doctor (by registration number - reg_no)


@app.route('/doctors/<reg_no>')
def findByReg(reg_no):
    if not 'username' in session:
        abort(401)

    return jsonify(doctorDao.findByReg(reg_no))

#curl "http://127.0.0.1:5000/doctors/18524"


@app.route('/doctors', methods=['POST'])
def createDoc():

    if not request.json:
        abort(400)  # check that the request has JSON data (if not returns a 400 error)

    doctor = {
        "reg_no": request.json["reg_no"],
        "firstName": request.json["firstName"],
        "lastName": request.json["lastName"],
        "specialty": request.json["specialty"]
    }  # read the request object and create a new doctor

    doctorAdd = doctorDao.createDoc(doctor)

    return jsonify(doctorAdd)

# curl -i -H "Content-Type:application/json" -X POST -d '{"reg_no":"18524","firstName":"Gavin","lastName":"Blake","specialty":"Cardiology"}' http://127.0.0.1:5000/doctors

#Windows:
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg_no\":\"18524\",\"firstName\":\"Gavin\",\"lastName\":\"Blake\",\"specialty\":\"Cardiology\"}" http://127.0.0.1:5000/doctors

#This is a put and it takes in the id from the url


@app.route('/doctors/<reg_no>', methods=['PUT'])
def updateDoc(reg_no):
    foundDoctor = doctorDao.findByReg(reg_no)

    #print (foundDoctor)

    if foundDoctor == {}:
        return jsonify({}), 404

    if not request.json:
        abort(400)

    currentDoctor = foundDoctor

    if 'reg_no' in request.json:
        currentDoctor['reg_no'] = request.json['reg_no']
    if 'firstName' in request.json:
        currentDoctor['firstName'] = request.json['firstName']
    if 'lastName' in request.json:
        currentDoctor['lastName'] = request.json['lastName']
    if 'specialty' in request.json:
        currentDoctor['specialty'] = request.json['specialty']

    doctorDao.updateDoc(currentDoctor)

    return jsonify(currentDoctor)

#curl -i -H "Content-Type:application/json" -X PUT -d '{"lastName":"Healy"}' http://127.0.0.1:5000/doctors/18524

#Windows:
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"lastName\":\"Healy\"}" http://127.0.0.1:5000/doctors/18524


@app.route('/doctors/<reg_no>', methods=['DELETE'])
def deleteDoc(reg_no):
    doctorDao.deleteDoc(reg_no)
    return jsonify({'Done': True})

#Run Flask
if __name__ == '__main__' :
    app.run(debug= True)
