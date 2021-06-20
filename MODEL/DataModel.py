
import pandas as pd
import sys
import config

def readFile(filePath):
        """this function will read the .csv file inside the work folder, named covid19-download.csv
        :param no parameters
        """
        # this portion set the view of prints form tables to no hide any column
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        # the try/except will catch any problem raised from the trying of open file
        try:
            # a global variable data was defined to be used outside the method readFile()

            # using pandas usecols is possible to specify exactly which column will be read from file
            data = pd.read_csv(config.filePath,
            ##defining only 100 rows to be read
                           nrows = 100,
            ##Records objects beeing passed to a data structure
                           usecols = ['pruid','prname','prnameFR','date','numconf','numprob',
                                      'numdeaths','numtotal','numtoday','ratetotal'])


        #if the file is unavailable or missing the exception will be handled and printed here
        except FileNotFoundError:
            print("JANIO MENDONCA JUNIOR")
            print ("Could not open the file or file not available")
            sys.exit()

        return data

def getOneRow(RowId):
    # this command will select only one Id
    row = config.data.iloc[[RowId]]
    return row

def getManyRows(RowNumbers):
    # this line will select many rows based on the ID supplied
    row = config.data.iloc[RowNumbers, :]
    return row

# Inserting Data provided by the user in memory data or writing it in a file
def insertData(Row):
    data = config.data.append(Row, ignore_index=True)
    config.data = data

def updateData (Id, Row):
    config.data.iloc[[int(Id)]] = Row

def deleteData (Id):
    index = int(Id)
    data = config.data.drop(index)
    config.data = data

def createNewCsv():
    config.data.to_csv(config.filePath, index=False)

