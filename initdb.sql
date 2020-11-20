  
use datarepresentation;

create table patients(
    -> id NOT NULL int AUTO_INCREMENT PRIMARY KEY,
    -> firstName varchar(250),
    -> lastName varchar(250),
    -> reasonForVisiting varchar(250)
    -> );