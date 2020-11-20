#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response, render_template
from PatientDao import patientDao

from flask_cors import CORS


#Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')

CORS(app)

#Saved in memory:array for storing the patients
#patients = [
 #   {
 #      "id":1,
 #     "firstName":"John",
 #       "lastName":"Ford",
 #       "reasonForVisiting":"HTN"
 #   },
 #   {
 #       "id":2,
 #       "firstName":"Amy",
 #       "lastName":"Duffy",
 #       "reasonForVisiting":"COPD"
 #   },
 #   {
 #       "id":3,
 #       "firstName":"Andrew",
 #       "lastName":"Murphy",
 #       "reasonForVisiting":"NIDDM"
 #   },
 #   {
 #       "id":4,
 #       "firstName":"Frances",
 #       "lastName":"Walsh",
 #       "reasonForVisiting":"CAD"
 #   },
 #   {
 #       "id":5,
 #       "firstName":"Emer",
 #       "lastName":"Byrne",
 #       "reasonForVisiting":"CD"
 #   },
 #   {
 #       "id":13,
 #       "firstName":"Orla",
 #       "lastName":"Kennedy",
 #       "reasonForVisiting":"HLD"
 #   },
 #   {
 #       "id":14,
 #       "firstName":"David",
 #       "lastName":"Smith",
 #       "reasonForVisiting":"IBD"
 #   },
 #   {
 #       "id":15,
 #       "firstName":"Mike",
 #       "lastName":"Sullivan",
 #       "reasonForVisiting":"RA"
 #   },
 #   {
 #       "id":16,
 #       "firstName":"Aoife",
 #       "lastName":"Reilly",
 #       "reasonForVisiting":"UTI"
 #   },
 #   {
 #       "id":17,
 #       "firstName":"Shane",
 #       "lastName":"Gallagher",
 #       "reasonForVisiting":"IBD"
 #   }
#]

#url map for /patients for method GET
#returns the list converted in JSON

@app.route('/patients')
def getAll():
    results = patientDao.getAll()
    return jsonify(results)
    #return jsonify({'patients':patients})
# curl -i http://localhost:5000/patients




#To find the ID by passing the info to the function as a String called 'id'
# filter searches through the list patients and returns only the ones that matches the id variable. lambda goes through each element of the list

@app.route('/patients/<int:id>')
def get_patient(id):
    foundPatient = patientDao.get_patient(id)
    return jsonify(foundPatient)

#curl -i http://localhost:5000/patients/7

@app.route('/patients', methods=['POST'])
def create_patient():

    if not request.json:
        abort(400) #check that the request has JSON data (if not returns a 400 error)
    if not 'id' in request.json:
        abort(400)

    patient={
        "firstName": request.json['firstName'],
        "lastName":request.json['lastName'],
        "reasonForVisiting":request.json['reasonForVisiting']
    } #read the request object and create a new patient

    values=(patient['firstName'],patient['lastName'],patient['reasonForVisiting'])
    newId= patientDao.create(values)
    patient['id']=newId
    return jsonify(patient)

# sample test
# curl -i -H "Content-Type:application/json" -X POST -d "{\"firstName\":\"Fiona\",\"lastName\":\"OBrien\",\"reasonForVisiting\":\""Obes\"}' http://localhost:5000/patients

#This is a put and it takes in the id from the url
@app.route('/patients/<int:id>', methods =['PUT'])
def update_patient(id):
    foundPatients=patientDao.get_patient(id)

    #print (foundPatients)

    if foundPatients == {}:
        return jsonify({}), 404

    if not foundPatients:
        abort(400)


    if 'firstName' in request.json:
        foundPatients['firstName'] = request.json['firstName']
    if 'lastName' in request.json:
        foundPatients['lastName'] = request.json['lastName']
    if 'reasonForVisiting' in request.json:
        foundPatients['reasonForVisiting'] = request.json['reasonForVisiting']

    values = (foundPatients['firstName'], 
              foundPatients['lastName'],
              foundPatients['reasonForVisiting'],
              foundPatients['id'])
    patientDao.update(values)
    return jsonify(foundPatients)

#curl -i -H "Content-Type:application/json" -X PUT -d '{"lastName":"OReilly"}' http://localhost:5000/patients/9

#Windows:
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"lastName\":\"OReilly\"}" http://localhost:5000/patients/9

@app.route('/patients/<int:id>', methods =['DELETE'])
def delete_patient(id):
    patientDao.delete_patient(id)
    return  jsonify( {'result':True })

#Run Flask
if __name__ == '__main__' :
    app.run(debug= True)