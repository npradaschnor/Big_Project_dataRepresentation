<h1 align="center"> Project 2020 - Flask app </h1><br>

<p align="center"><img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center"></p>
<h2 align="center"> Higher Diploma in Science in Data Analytics</h2>
<h2 align="center">Data Representation and Querying Module</h2></p>

<h3 align="center"><i>Noa P Prada Schnor | G00364704<i> </h3><br><br>

---------------------------------------------------------------------------------------------------------------------------------------------------------------


##### This folder contains the final project for the Data Representation and Querying Module.

#### The project contains the following files:

|    File                       |      Description                                                                                       | 
|:------------------------------|:-------------------------------------------------------------------------------------------------------|
| [initdb.sql](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/initdb.sql)                    |   SQL code to create the database, create the tables and populate the tables                             |
| [dbconfig.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/dbconfig.py)                   |   Configuration file for DAO                                                                           |
| dbconfigtemplate.py           |   Configuration file template for DAO                                                                  |
| [PatientDao.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/PatientDao.py)                 |   DAO Pattern - CRUD operations for patients database                                                                       |
| [DoctorDao.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/DoctorDao.py)                 |   DAO Pattern - CRUD operations for doctors database                                                                       |
| [app.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/app.py)                        |   Flask server that implements a REST API that performs CRUD operations and authorization(logging in)  |
| templates/[home.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/home.html)           |   HTML for home page                                                                                   |
| templates/[patientviewer.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/patientviewer.html)  |   HTML that uses AJAX to link to the server and provide a user interface for patients database                              |
| templates/[doctorviewer.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/doctorviewer.html)           |   HTML that uses AJAX to link to the server and provide a user interface for doctors database                                                                                   |
| templates/[login.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/login.html)  |   HTML that contains the login form  |
| requirements.txt              |   List of necessary packages                                                                           |

### :mega:  My web server is hosted on :computer: [PythonAnywhere](http://npradaschnor.pythonanywhere.com/)

### Login details

| |User1|User2|
|:----:|:----:|:----:|
|username| AndrewBeatty1 | dataRep2020  |
|password| dataStudent   | GMIT2020  |



--------------------------------------------------------------------------------------------------------------------------------------------------------------

### To run the code check if you have already installed:
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [Flask](https://flask.palletsprojects.com/en/master/installation/)
- [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
- [Python 3.6.3](https://www.python.org/downloads/release/python-363/)

#### Also check the [requirements.txt] (xxxxxx) to see the libraries used and their version.

*Note*: Most of the languages/packages were included in the Anaconda programme. However, some of them were called through 'pip' on the command line or downloaded from the internet.

*Note 2*: The computer system worked from is windows 10.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

### :ballot_box_with_check: **Instructions on how to run the project**

#### :arrow_forward: **Step 1.** 
#### Clone the repository to your machine using the following HTTPS:
:link: <https://github.com/npradaschnor/Big_Project_dataRepresentation.git>

#### :arrow_forward: **Step 2.**
#### Open a virtual environment within the project folder of the repository.

#### :arrow_forward: **Step 3.**
#### Check the requirements.txt file and install all the packages needed using the command:
- pip install -r path/to/requirements.txt

#### :arrow_forward: **Step 4.** 
#### Start mysql server. I've used [WAMPSERVER](https://www.wampserver.com/en/)

#### :arrow_forward: **Step 5.** 
#### To create the database, the tables (patients, doctors, users) and to insert data into the tables use the command code of the following file:
- initdb.sql

#### :arrow_forward: **Step 6.** 
#### Run the Flask server named app.py

#### :arrow_forward: **Step 7.** 
#### Type :link: <http://127.0.0.1:5000/> into your browser.

#### :arrow_forward: **Step 8.** 
#### Also check the following routes:
:link: <http://127.0.0.1:5000/patients> <br/>
:link: <http://127.0.0.1:5000/patientdata>

| Route                 | Result                        |
:-----------------------|:------------------------------|
|/                      |Redirects to /login route      |
|/login                 |Login page                     |
|/home                  |Renders home template          |
|/patients              |Retrieves patients records     |
|/patients/<id>         |Retrieves patient's record     |
|/patientdata           |Renders patientviewer template |
|/doctordata            |Renders doctorviewer template  |
|/doctors               |Retrieves doctors data         |
|/doctors/<reg_no>      |Retrieves doctor's data        |


#### :arrow_forward: **Step 9.**
#### Perform CRUD (Create, Read, Update and Delete) operations on the patients table.
