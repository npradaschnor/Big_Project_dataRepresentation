<h1 align="center"> Project 2020 - Flask app (<i>Python</i>)</h1><br>

<p align="center"><img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center"></p>
<h2 align="center"> Higher Diploma in Science in Data Analytics</h2>
<h2 align="center">Data Representation and Querying Module</h2></p>

<h3 align="center"><i>Noa P Prada Schnor  G00364704<i> </h3><br><br>

## This folder contains the final project for the Data Representation and Querying Module.

## The project contains the following files:

- initdb.sql
- patientdata.sql
- patientDao.py
- dbconfigtemplate.py
- dbconfig.py
- app.py
- home.html
- patientviewer.html
- requirements.txt

### The project contains:
1. A Flask server that implements a REST API file (app.py) [https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/app.py] (that performs CRUD operations and authorization (logging in)
2. One database table (from mySQL server: database named datarepresentation, table called patients). The file (initdb.sql) [https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/initdb.sql] has the create command for the table
3. A configuration file for DAO - (PatientDao.py)   [https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/PatientDao.py]
4. The (templates) [https://github.com/npradaschnor/Big_Project_dataRepresentation/tree/master/templates] folder that has HTML that use AJAX to link to the server and provide a user interface (homepage.html & patientviewer.html)
   
My web server is hosted on (PythonAnywhere) [http://npradaschnor.pythonanywhere.com/]

To run the code check if you have already installed:
(mysql-connector-python) [https://pypi.org/project/mysql-connector-python/]
(Flask) [https://flask.palletsprojects.com/en/master/installation/]
(Python 3.6.3) or newer versions [https://www.python.org/downloads/release/python-363/]

Also check the (requirements.txt) [] to see the libraries used and their version.

Note: Most of the languages were included in the Anaconda programme, the ones that weren't were called through 'pip' on the command line or downloaded from the internet.

Note 2: The computer system worked from is windows 10.

## Instructions on how to run the project:

### Step 1. 
##### Clone the repository to your machine.

### Step 2. 
##### Open a virtual environment within the project folder of the repository.

### Step 3. 
##### Check the requirements.txt file and install all the packages needed using the command:
- pip install -r path/to/requirements.txt

### Step 3. 
##### Start mysql server. I've used (WAMPSERVER) [https://www.wampserver.com/en/]

### Step 4. 
##### To create the database, the table and to insert the data into the table use the command code of the following files:
- initdb.sql

### Step 5. 
##### Run the Flask server named app.py

### Step 6. 
##### Type http://127.0.0.1:5000/ into your browser

### Step 7. 
##### Also check the following webpages
- http://127.0.0.1:5000/patients
- http://127.0.0.1:5000/patientdata

### Step 8.
##### Perform CRUD (Create, Read, Update and Delete) operations on the patients table
