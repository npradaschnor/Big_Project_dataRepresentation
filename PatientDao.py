import mysql.connector
from mysql.connector import cursor

class PatientDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        #print ("connection made")

    def create_patient(self, patient):
        cursor = self.db.cursor()
        sql = "insert into patients (id, firstName, lastName, reasonForVisiting) values (%s,%s,%s,%s)"
        values = [
            patient['id'],
            patient['firstName'],
            patient['lastName'],
            patient['reasonForVisiting'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

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

        return returnArray

    def get_patient(self, id):
        cursor = self.db.cursor()
        sql = 'select * from patients where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update_patient(self, patient):
       cursor = self.db.cursor()
       sql = "update patients set firstName = %s, lastName = %s, reasonForVisiting = %s where id = %s"
       values = [
           patient['firstName'],
           patient['lastName'],
           patient['reasonForVisiting'],
           patient['id']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return patient

    def delete_patient(self, id):
       cursor = self.db.cursor()
       sql = 'delete from patients where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['id','firstName', 'lastName', 'reasonForVisiting']
        patient = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                patient[colName] = value
        return patient

patientDao = PatientDao()