import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg


class PatientDao:
    db = ""

    def __init__(self):

        #Connect the MySQL Database
        self.db = mysql.connector.connect(host=cfg.mysql['host'],
                                          user=cfg.mysql['user'],
                                          password=cfg.mysql['password'],
                                          database=cfg.mysql['database'],
                                          port='3306')
        #print ("connection made")

#Add new patient to patients table (datarepresentation database on mysql)
    def create(self, patient):
        cursor = self.db.cursor()
        sql = "insert into patients (id,firstName, lastName, reasonForVisiting) values (%s,%s,%s,%s)"
        values = [
            patient['id'], patient['firstName'], patient['lastName'],
            patient['reasonForVisiting']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

#Get all the patients records from the patients table
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from patients'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

#Find a specific patient's record by id
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from patients where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

#Update a patient's record
    def update(self, patient):
        cursor = self.db.cursor()
        sql = "update patients set firstName = %s, lastName = %s, reasonForVisiting = %s where id = %s"
        values = [
            patient['firstName'], patient['lastName'],
            patient['reasonForVisiting'], patient['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return patient

#Delete a patient's record from patients table
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from patients where id = %s'
        values = [id]
        cursor.execute(sql, values)

        #self.db.commit()
        cursor.close()
        return {}

#Convert a list to dictionary
    def convertToDict(self, result):
        colnames = ['id', 'firstName', 'lastName', 'reasonForVisiting']
        patient = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                patient[colName] = value

        return patient


patientDao = PatientDao()