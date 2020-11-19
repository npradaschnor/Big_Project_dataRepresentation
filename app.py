#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response, render_template

from flask_cors import CORS


#Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='')

CORS(app)

#Saved in memory:array for storing the patients
patients = [
    {
        "id":1,
        "firstName":"John",
        "lastName":"Ford",
        "reasonForVisiting":"HTN"
    },
    {
        "id":2,
        "firstName":"Amy",
        "lastName":"Duffy",
        "reasonForVisiting":"COPD"
    },
    {
        "id":3,
        "firstName":"Andrew",
        "lastName":"Murphy",
        "reasonForVisiting":"NIDDM"
    },
    {
        "id":4,
        "firstName":"Frances",
        "lastName":"Walsh",
        "reasonForVisiting":"CAD"
    },
    {
        "id":5,
        "firstName":"Emer",
        "lastName":"Byrne",
        "reasonForVisiting":"CD"
    },
    {
        "id":6,
        "firstName":"Orla",
        "lastName":"Kennedy",
        "reasonForVisiting":"HLD"
    },
    {
        "id":7,
        "firstName":"David",
        "lastName":"Smith",
        "reasonForVisiting":"IBD"
    },
    {
        "id":8,
        "firstName":"Mike",
        "lastName":"Sullivan",
        "reasonForVisiting":"RA"
    },
    {
        "id":9,
        "firstName":"Aoife",
        "lastName":"Reilly",
        "reasonForVisiting":"UTI"
    },
    {
        "id":10,
        "firstName":"Shane",
        "lastName":"Gallagher",
        "reasonForVisiting":"IBD"
    }
]

@app.route('/home')
def home():
    pagetitle = "HomePage"
    return render_template('home.html', mytitle=pagetitle)

@app.route('/patientdata')
def patient_table():
    return render_template('patientviewer.html')

#url map for /patients for method GET
#returns the list converted in JSON
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify({'patients':patients})
# curl -i http://localhost:5000/patients


#To find the ID by passing the info to the function as a String called 'id'
# filter searches through the list patients and returns only the ones that matches the id variable. lambda goes through each element of the list
@app.route('/patients/<string:id>', methods =['GET'])
def get_patient(id):
    foundPatients = list(filter(lambda t: t['id'] == id, patients))

    if len(foundPatients) == 0:
        return jsonify( {'patient' : '' }),204 #if nothing is returned send back an empty patient, with status 204
    return jsonify( {'patient' : foundPatients[0] }) #otherwise send back a JSON object - the 1st of the found patients

#curl -i http://localhost:5000/patients/7

@app.route('/patients', methods=['POST'])
def create_patient():
    

    if not request.json:
        abort(400) #check that the request has JSON data (if not returns a 400 error)
    if not 'id' in request.json:
        abort(400)

    patient={
        "id":  request.json['id'],
        "firstName": request.json['firstName'],
        "lastName":request.json['lastName'],
        "reasonForVisiting":request.json['reasonForVisiting']
    } #read the request object and create a new patient

    patients.append(patient) #append it to the list patient
    
    return jsonify( {'patient':patient }),201 #returns what was just added

# sample test
# curl -i -H "Content-Type:application/json" -X POST -d "{\"firstName\":\"Fiona\",\"lastName\":\"OBrien\",\"reasonForVisiting\":\""Obes\"}' http://localhost:5000/patients

#This is a put and it takes in the id from the url
@app.route('/patients/<string:id>', methods =['PUT'])
def update_patient(id):
    foundPatients=list(filter(lambda t : t['id'] ==id, patients)) #searches through the list of patients using lambda function
    if len(foundPatients) == 0:
        abort(404) #if patient is not found
    if not request.json:
        abort(400) #check if the JSON in the request is properly formatted
    if 'firstName' in request.json and type(request.json['firstName']) != str:
        abort(400) #if make is not a type of string returns 400 error
    if 'lastName' in request.json and type(request.json['lastName']) is not str:
        abort(400)
    if 'reasonForVisiting' in request.json and type(request.json['reasonForVisiting'])  is not str:
        abort(400)
    
    currentPatient = foundPatients[0]

    if 'firstName' in request.json:
        currentPatient['firstName']  = request.json['firstName']

    if 'lastName' in request.json:
        currentPatient['lastName'] =request.json['lastName']

    if reasonForVisiting in request.json:
        currentPatient['reasonForVisiting'] =request.json['reasonForVisiting']

    return jsonify(currentPatient) #returns the updated patient

#curl -i -H "Content-Type:application/json" -X PUT -d '{"lastName":"OReilly"}' http://localhost:5000/patients/9

#Windows:
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"lastName\":\"OReilly\"}" http://localhost:5000/patients/9

#Similar to previous functions. using the lambda function to find the patient by the id variable. If found it is deleted and it returns a JSON that says the result is True
@app.route('/patients/<string:id>', methods =['DELETE'])
def delete_patient(id):
    foundPatients = list(filter (lambda t : t['id'] == id, patients))
    if len(foundPatients) == 0:
        abort(404)
    patients.remove(foundPatients[0])
    return  jsonify( {'result':True })

#Handles error 404 and 400
@app.errorhandler(404)
def not_found404(error):
    return make_response(jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response(jsonify( {'error':'Bad Request'}), 400)

#Run Flask
if __name__ == '__main__' :
    app.run(debug= True)