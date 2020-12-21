  
-- Command to create the database 'datarepresentation'
CREATE DATABASE datarepresentation;

--Select the database 'datarepresentation' for use
USE datarepresentation;


------------------PATIENTS-----------------------

--Create table 'patients' | Patients Database
CREATE TABLE patients (
    id CHAR (11) NOT NULL,
    firstName VARCHAR (250),
    lastName VARCHAR (250),
    reasonForVisiting VARCHAR (250)
    PRIMARY KEY(id)
);

-- Check if the table 'patients' was created as expected
DESC patients;

--Populate the table 'patients'
INSERT INTO patients VALUES
('R3650A', 'Orla', 'Hennessy', 'HLD'),
('F4386D', 'Frances', 'Walsh', 'CAD'),
('G9340E', 'Lara', 'Byrne', 'CD'),
('S7326D', 'David', 'Smith', 'IBD'),
('N2805A', 'Michael', 'Sullivan', 'RA'),
('G1714E', 'Shane', 'Gallagher', 'IBD'),
('S5147C', 'Francis', 'Dunne', 'CAD'),
('R4576C', 'Rebecca', 'Watts', 'OBES'),
('R2345C', 'Lisa', 'Duffy', 'IDA');


--------------------- DOCTORS --------------------------

--Create table 'doctors' | Doctors Database

CREATE TABLE doctors (
    reg_no int(250) NOT NULL,
    firstName varchar(250) NOT NULL,
    lastName varchar(250) NOT NULL,
    specialty varchar(250) NOT NULL,
    PRIMARY KEY (reg_no)
);

-- Check if the table 'doctors' was created as expected
DESC doctors;

--Populate the table 'doctors'
INSERT INTO doctors VALUES
(18524, 'Gavin', 'Blake', 'Cardiology'),
(22932, 'Gayle', 'Bennett', 'Gastroenterology'),
(38585, 'Donal', 'Brennan', 'Gynaecology'),
(36361, 'Emily', 'Harrold', 'Oncology');


----------------------- USERS -------------------------------

--Create table 'users' | Login
CREATE TABLE users (
    id INT (11) NOT NULL AUTO_INCREMENT,
    username VARCHAR (250),
    password VARCHAR (250),
    PRIMARY KEY(id)
);

-- Check if the table 'users' was created as expected
DESC users;

--Populate the table 'users'
INSERT INTO users VALUES
('AndrewBeatty1', 'dataRep2020'),
('dataStudent', 'GMIT2020');