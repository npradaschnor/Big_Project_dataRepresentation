  
use datarepresentation;

create table patients(
    -> id char(11) NOT NULL,
    -> firstName varchar(250),
    -> lastName varchar(250),
    -> reasonForVisiting varchar(250)
    -> PRIMARY KEY(id)
    -> );