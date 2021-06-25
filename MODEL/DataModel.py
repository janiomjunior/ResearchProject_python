"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 25/06/2021
Version: 2.0

This file is responsible to make the MODEL part of MVC, where all the DataFrame access are done, such as
the CRUD operations and communications with controller.
"""
import pandas as pd
import sys
import config

def readFile(filePath):
        """ this function will read the .csv file inside the work folder, named covid19-download.csv

            Args:
                date_input: the .csv path to be read
            Returns:
                True: for a valid format YYYY-MM-DD
                False: for a invalid format
            Raises:
                FileNotFoundError: If cannot open or not available file
        """

        #this portion set the view of prints form tables to no hide any column
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
    """ will read just one line from DataFrame in memory

        Args:
            RowId: the row Id supplied by the user
        Returns:
            row: the row found on DataFrame
    """

    # this command will select only one Id

    row = config.data.iloc[[RowId]]
    return row

def getManyRows(RowNumbers):
    """ will read multiples line from DataFrame in memory

        Args:
            RowNumbers: a array of row Index to be read
        Returns:
            row: a list of arrays found
    """
    # this line will select many rows based on the ID supplied
    row = config.data.iloc[RowNumbers, :]
    return row


def insertData(Row):
    """ Inserting Data provided by the user in memory data

       Args:
           Row: a array to be inserted
       Returns:
           none
    """
    data = config.data.append(Row, ignore_index=True)
    config.data = data

def updateData (Id, Row):
    """ Will update the data from provided ID row

       Args:
           Row: a replace row
           Id: the row Id to be updated
       Returns:
           none
    """
    config.data.iloc[[int(Id)]] = Row

def deleteData (Id):
    """ Will delete the data from provided ID with row

       Args:
           Id: the row Id
       Returns:
           none
    """
    index = int(Id)
    data = config.data.drop(index)
    config.data = data

def createNewCsv():
    """ Will create new file with the modified DataFrame

       Args:
           none
       Returns:
           none
    """
    config.data.to_csv(config.newFilePath, index=False)

