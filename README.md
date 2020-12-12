<h1 align="center"> Project 2020 - Flask app </h1><br>

<p align="center"><img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center"></p>
<h2 align="center"> Higher Diploma in Science in Data Analytics</h2>
<h2 align="center">Data Representation and Querying Module</h2></p>

<h3 align="center"><i>Noa P Prada Schnor | G00364704<i> </h3><br><br>

---------------------------------------------------------------------------------------------------------------------------------------------------------------


### This folder contains the final project for the Data Representation and Querying Module.

### The project contains the following files:

|    File                       |      Description                                                                                       | 
|:------------------------------|:-------------------------------------------------------------------------------------------------------|
| [initdb.sql](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/initdb.sql)                    |   SQL code to create the database, create the table and populate the table                             |
| [dbconfig.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/dbconfig.py)                   |   Configuration file for DAO                                                                           |
| dbconfigtemplate.py           |   Configuration file template for DAO                                                                  |
| [PatientDao.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/PatientDao.py)                 |   DAO Pattern - CRUD operations                                                                        |
| [app.py](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/app.py)                        |   Flask server that implements a REST API that performs CRUD operations and authorization(logging in)  |
| templates/[home.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/home.html)           |   HTML for home page                                                                                   |
| templates/[patientviewer.html](https://github.com/npradaschnor/Big_Project_dataRepresentation/blob/master/templates/patientviewer.html)  |   HTML that uses AJAX to link to the server and provide a user interface                               |
| requirements.txt              |   List of necessary packages                                                                           |

#### My web server is hosted on [PythonAnywhere](http://npradaschnor.pythonanywhere.com/)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

### To run the code check if you have already installed:
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [Flask](https://flask.palletsprojects.com/en/master/installation/)
- [Python 3.6.3](https://www.python.org/downloads/release/python-363/)

#### Also check the [requirements.txt] (xxxxxx) to see the libraries used and their version.

*Note*: Most of the languages/packages were included in the Anaconda programme. However, some of them were called through 'pip' on the command line or downloaded from the internet.

*Note 2*: The computer system worked from is windows 10.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Instructions on how to run the project:

#### **Step 1.** 
#### Clone the repository to your machine using the following HTTPS:
- https://github.com/npradaschnor/Big_Project_dataRepresentation.git

#### **Step 2.**
#### Open a virtual environment within the project folder of the repository.

#### **Step 3.**
#### Check the requirements.txt file and install all the packages needed using the command:
- pip install -r path/to/requirements.txt

#### **Step 4.** 
#### Start mysql server. I've used [WAMPSERVER](https://www.wampserver.com/en/)

#### **Step 5.** 
#### To create the database, the table and to insert the data into the table use the command code of the following files:
- initdb.sql

#### **Step 6.** 
#### Run the Flask server named app.py

#### **Step 7.** 
#### Type <http://127.0.0.1:5000/> into your browser.

#### **Step 8.** 
#### Also check the following webpages:
- <http://127.0.0.1:5000/patients>
- <http://127.0.0.1:5000/patientdata>

#### **Step 9.**
#### Perform CRUD (Create, Read, Update and Delete) operations on the patients table.
