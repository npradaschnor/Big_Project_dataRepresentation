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
                                          database=cfg.mysql['database'])
        #print ("connection made")

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

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from patients where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

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

    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from patients where id = %s'
        values = [id]
        cursor.execute(sql, values)

        #self.db.commit()
        cursor.close()
        return {}

    def convertToDict(self, result):
        colnames = ['id', 'firstName', 'lastName', 'reasonForVisiting']
        patient = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                patient[colName] = value

        return patient


patientDao = PatientDao()