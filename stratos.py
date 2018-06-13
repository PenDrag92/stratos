import time, os, sys, sqlite3
from datetime import datetime



######################################################
################ GLOBAL VARIABLES ####################
######################################################
DATABASE = "C:\\sqlite\db\pythonsqlite.db"
TABLE1 = "myTable1"
TABLE2 = "myTable2"



######################################################
########## CLASS THAT GETS THE DATA FILE #############
######################################################
class GetNewFile:

    def __init__(self):

        self.file = None
        self.path = None
        self.possibleFiles = []
        self.dates = []

        self. getFiles()
        self.getLatestFile()


    #method that gets the .txt files in the folder
    def getFiles(self):

        self.path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])

        for (path, directories, files) in os.walk( self.path ):
            for fileName in files:
                if ".txt" in fileName:
                    self.possibleFiles.append(fileName)


    #method that finds the latest data file
    def getLatestFile(self):

        for fileName in self.possibleFiles:
            self.dates.append( datetime( int(fileName[0:4]), int(fileName[4:6]), int(fileName[6:8]), int(fileName[8:10]), int(fileName[10:12]), int(fileName[12:14]) ) )

        newest = max(self.dates)
        index = self.dates.index(newest)

        self.file = self.possibleFiles[index]



######################################################
########## CLASS THAT PROCESSES THE DATA #############
######################################################
class ProcessFile:

    def __init__(self, fileName):

        self.fileName = fileName
        self.codeNames = []
        self.data = {}
        self.queryParameters = []

        self.readData()
        self.obtainParameterNames()


    #method that reads the data and stores it into a dictionary
    def readData(self):

        print("opening file: " + str(self.fileName))
        f = open(self.fileName,'r')
        line = f.readlines()[-1]
        data = line.split(";")

        for parameter in data[1:]:

            splittedParameter = parameter.split(":")
            self.data[ splittedParameter[0] ] = splittedParameter[1]

        print("data gathered:  " + str(self.data))


    #method that gets the parameter names for each code from the SQL db
    def obtainParameterNames(self):

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        for code in self.data:
            query = "SELECT name FROM " + TABLE1 + " WHERE code = " + code + ";"
            cursor.execute(query)
            results = cursor.fetchall()
            self.codeNames.append(results[0][0])

        cursor.close()
        connection.close()

        print("parameters received:   " + str(self.codeNames))


    #method that adds the recent processed info to a database in the server
    # def actualizeDatabase(self):
    #     connection = sqlite3.connect(DATABASE)
    #     cursor = connection.cursor()
    #
    #
    #     cursor.close()
    #     connection.close()



######################################################
#################  MAIN PROGRAM ######################
######################################################
if __name__ == "__main__":

    os.system("cls")
    fileGetter = GetNewFile()
    processObject = ProcessFile( fileGetter.file )




##
