import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg


class DoctorDao:
    db = ""

    def __init__(self):

        #Connect the MySQL Database
        self.db = mysql.connector.connect(host=cfg.mysql['host'],
                                          user=cfg.mysql['user'],
                                          password=cfg.mysql['password'],
                                          database=cfg.mysql['database'],
                                          port='3306')
        #print ("connection made")

#Add new doctor to doctors table (datarepresentation database on mysql)
    def createDoc(self, doctor):
        cursor = self.db.cursor()
        sql = "insert into doctors (reg_no,firstName, lastName, specialty) values (%s,%s,%s,%s)"
        values = [
            doctor['reg_no'], doctor['firstName'], doctor['lastName'],
            doctor['specialty']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

#Get all the doctors records from the doctors table
    def getAllDoc(self):
        cursor = self.db.cursor()
        sql = 'select * from doctors'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

#Find a specific doctor's record by reg_no
    def findByReg(self, reg_no):
        cursor = self.db.cursor()
        sql = 'select * from doctors where reg_no = %s'
        values = [reg_no]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

#Update a doctor's record
    def updateDoc(self, doctor):
        cursor = self.db.cursor()
        sql = "update doctors set firstName = %s, lastName = %s, specialty = %s where reg_no = %s"
        values = [
            doctor['firstName'], doctor['lastName'],
            doctor['specialty'], doctor['reg_no']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return doctor

#Delete a doctor's record from doctors table
    def deleteDoc(self, reg_no):
        cursor = self.db.cursor()
        sql = 'delete from doctors where reg_no = %s'
        values = [reg_no]
        cursor.execute(sql, values)

        #self.db.commit()
        cursor.close()
        return {}

#Convert a list to dictionary
    def convertToDict(self, result):
        colnames = ['reg_no', 'firstName', 'lastName', 'specialty']
        doctor = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                doctor[colName] = value

        return doctor


doctorDao = DoctorDao()