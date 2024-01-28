import sqlite3
import traceback
import sys
import os
import base64
from PIL import Image

class DataBase():

    def __init__(self,dataBasePath,sqlCursor=None):
        self.dataBasePath=dataBasePath
        self.sqliteConnection=None
        self.sqlCursor = sqlCursor

    def OpenDataBase(self):
        try:
            connection = sqlite3.connect(self.dataBasePath)
            self.sqlCursor= connection.cursor()
            self.sqliteConnection=connection
            print('database connected.')
            return True
        except Exception as ex:
            print('database connection error has occured.')
            traceback.print_exception(ex)
            return False
        
    def closeDataBase(self):
        self.sqliteConnection.close()

    # need to make prettier
    def convertToBinaryData(self,filename) -> tuple:
        name = os.path.basename(filename).split('.')[0]
        mode=None
        size=None
        binaryData=None
        # Convert digital data to binary format
        with Image.open(filename) as file:
            #binaryData = file.read()
            mode = file.mode
            size = file.size
            #binaryData = base64.b64encode(file)        
        with open(filename, 'rb') as file:
            binaryData = file.read()
            binaryData = base64.b64encode(binaryData)
        tupleOfValues=(name,binaryData,str(mode),str(size))     
        return tupleOfValues
    
#TRYING THIS->
    def cBinary(self,fileName):
        with open(fileName, "rb") as file:
            binaryData = file.read()
        return binaryData
    
    def writeTofile(self,data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)
        print("Stored blob data into: ", filename, "\n")

    #turn this into a generic read statement
    def readBlobData(self,empId):
        try:
            tupleinfo=None
            #sqliteConnection = sqlite3.connect('sqliteData//tokensDataBase')
            #cursor = sqliteConnection.cursor()
            sql_fetch_blob_query = """SELECT * from tokens where id = ?"""
            self.sqlCursor.execute(sql_fetch_blob_query, (empId,))
            record = self.sqlCursor.fetchall()
            for row in record:
                #print("Id = ", row[0], "Name = ", row[1])
                name=row[1]
                photo = row[2]
                mode = row[3]
                size = row[4]
                tupleinfo = (name,photo,mode,size)
                #resumeFile = row[3]

                #print("Storing employee image and resume on disk \n")
                #photoPath = "test" + str(name) + ".jpg"
                #resumePath = "E:\pynative\Python\photos\db_data\\" + name + "_resume.txt"
                #self.writeTofile(photo, photoPath)
            #self.sqlCursor.close()
            return tupleinfo

        except sqlite3.Error as error:
            print("Failed to read blob data from sqlite table", error)
        #finally:
            #if self.sqliteConnection:
                #self.sqliteConnection.close()
                #print("sqlite connection is closed")

    def insertBLOB(self,photo):
        try:
            binary = self.cBinary(photo)
            t=("test",binary,1,1)
            sqliteConnection = sqlite3.connect('sqliteData//TokensDB')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_insert_blob_query = f""" INSERT INTO Tokens
                                    (name,token, mode, size) VALUES (?,?,?,?)"""
            #sqlite_insert_blob_query = """ select * from sqlite_master where type='table'"""

            #empPhoto = photo.tobytes()
            #resume = convertToBinaryData(resumeFile)
            # Convert data into tuple format
            #data_tuple = (values[0],str(values[1]),str(values[2]))
            cursor.execute(sqlite_insert_blob_query,t)
            sqliteConnection.commit()
            print("Image and file inserted successfully as a BLOB into a table:", cursor.fetchall())
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("the sqlite connection is closed")

#insertBLOB(1, "Tokens/mapMarker.png")
#image = Image.open("Tokens/mapMarker.png")
#mode = image.mode
#size = image.size
#DataBase(None).insertBLOB("Tokens/transparentMapMarker.png")
#DataBase(None).insertBLOB("Test/mapMarker_noBG.png")
