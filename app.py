#!flask/bin/python
from flask import Flask, url_for, jsonify, session, request, abort, make_response, render_template, redirect
from PatientDao import patientDao 

#Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')

app.secret_key = 'k9WydtaAVn9E2HmHy0T3VvcRHJzdDZQp'

#Need to login to access the homepage and patientdata
@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))

    return 'Welcome, ' + session['username'] +\
        '<br><a href="'+url_for('logout')+'">Logout</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return '<br/><h1 style="font-family:verdana"><b> LOGIN </b></h1><br/> '+\
    '<button style="font-family:verdana, text-decoration:none">'+\
    '<a href="'+url_for('proccess_login')+'">' +\
    'Login' +\
    '</a>' +\
    '</button>'

@app.route('/processlogin')
def proccess_login():
    #check credentials
    #if bad redirect to login page again

    #else
    session['username'] = "Andrew"
    return redirect(url_for('homepage'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

#/home route renders home template
@app.route('/home')
def homepage():
    pagetitle = "HomePage"

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('home.html', mytitle=pagetitle)


# /patiendata route renders patientviewer template
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
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"W9146A\",\"firstName\":\"Fiona\",\"lastName\":\"OBrien\",\"reasonForVisiting\":\""OBES\"}" http://127.0.0.1:5000/patients

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

#Run Flask
if __name__ == '__main__' :
    app.run(debug= True)
