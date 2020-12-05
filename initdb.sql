  
-- Command to create the database 'datarepresentation'
CREATE DATABASE datarepresentation;

--Select the database 'datarepresentation' for use
USE datarepresentation;

--Create table 'patients'
CREATE TABLE patients (
    -> id CHAR (11) NOT NULL,
    -> firstName VARCHAR (250),
    -> lastName VARCHAR (250),
    -> reasonForVisiting VARCHAR (250)
    -> PRIMARY KEY(id)
    -> );

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

