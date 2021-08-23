"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 29/07/2021
Assignment 4
Version: 4.0

This file is responsible to make the MODEL part of MVC, where all the Database access are done, such as
the CRUD operations and communications with controller.
"""
import sqlite3
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
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
            config.data = pd.read_csv(config.filePath,
            ##defining only 100 rows to be read
                           #nrows = 100,
            ##Records objects beeing passed to a data structure
                           usecols = ['pruid','prname','prnameFR','date','numconf','numprob',
                                      'numdeaths','numtotal','numtoday','ratetotal'])

            #print(data)
        #if the file is unavailable or missing the exception will be handled and printed here
        except FileNotFoundError:
            print("JANIO MENDONCA JUNIOR")
            print ("Could not open the file or file not available")
            sys.exit()

        #creating the database and table to persist data from .csv file into database
        global conn
        try:
            conn = sqlite3.connect('COVID19_DB')
            c = conn.cursor()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        #global c
        c = conn.cursor()
        config.data.to_sql('COVID19', conn, if_exists='replace')
        c.execute('''  SELECT * FROM COVID19  ''')
        config.data = DataFrame(c.fetchall(), columns=['index','pruid','prname','prnameFR','date','numconf','numprob',
                                      'numdeaths','numtotal','numtoday','ratetotal'])

def getOneRow(RowId):
    """ will read just one line from DataFrame in memory

        Args:
            RowId: the row Id supplied by the user
        Returns:
            row: the row found on DataFrame
    """

    # this command will select only one Id

    config.row = pd.read_sql_query('SELECT * FROM COVID19 WHERE `index` = (?)', conn, params=(RowId,))
    return config.row

def getManyRows(RowNumbers):
    """ will read multiples line from DataFrame in memory

        Args:
            RowNumbers: a array of row Index to be read
        Returns:
            row: a list of arrays found
    """
    # this line will select many rows based on the ID supplied
    query = "SELECT * FROM COVID19 WHERE"
    rowId_size = len(RowNumbers)
    fixed = ""
    rowindex = 0
    my_input = []
    if (rowId_size > 2):
        while (rowindex < rowId_size):
            if(rowindex < rowId_size-1  ):
                fixed += " `index` = (?) OR "
            else:
                fixed += " `index` = (?) "
            my_input.append(RowNumbers[rowindex])
            rowindex += 1
    prepared_statement = query + fixed
    i = 0
    result = pd.read_sql_query(prepared_statement, conn, params=(my_input))
    config.row = result
    return config.row

def insertData(Row):
    """ Inserting Data provided by the user in COVID19 table

       Args:
           Row: a array to be inserted
       Returns:
           none
    """

    prepared_statement = "INSERT INTO COVID19(pruid,prname,prnameFR,date,numconf,numprob,numdeaths,numtotal,numtoday,ratetotal) VALUES (?,?,?,?,?,?,?,?,?,?)"
    c = conn.cursor()
    c.execute(prepared_statement, [Row['pruid'], Row['prname'], Row['prnameFR'], Row['date'], Row['numconf'], Row['numprob'], Row['numdeaths'], Row['numtotal'], Row['numtoday'],Row['ratetotal']])
    conn.commit()
    c.execute('''  SELECT * FROM COVID19  ''')
    config.data = DataFrame(c.fetchall(), columns=['index', 'pruid', 'prname', 'prnameFR', 'date', 'numconf', 'numprob',
                                                   'numdeaths', 'numtotal', 'numtoday', 'ratetotal'])

def updateData (Id, Row):
    """ Will update the data provided by the user on the database COVID19 table

       Args:
           Row: a replace row
           Id: the row Id to be updated
       Returns:
           none
    """
    Row['index'] = Id
    prepared_statement = "UPDATE COVID19 SET pruid=?,prname=?,prnameFR=?,date=?,numconf=?,numprob=?,numdeaths=?,numtotal=?,numtoday=?,ratetotal=? WHERE `index`= ? "
    c = conn.cursor()
    c.execute(prepared_statement, [Row['pruid'], Row['prname'], Row['prnameFR'], Row['date'], Row['numconf'], Row['numprob'], Row['numdeaths'], Row['numtotal'], Row['numtoday'],Row['ratetotal'], Row['index']] )
    conn.commit()
    c.execute('''  SELECT * FROM COVID19  ''')
    config.data = DataFrame(c.fetchall(), columns=['index', 'pruid', 'prname', 'prnameFR', 'date', 'numconf', 'numprob',
                                                   'numdeaths', 'numtotal', 'numtoday', 'ratetotal'])

def deleteData (Id):
    """ Will delete the row on database, based on the Id provided

       Args:
           Id: the row Id
       Returns:
           none
    """
    prepared_statement = "DELETE FROM COVID19 WHERE `index` = ?"
    c = conn.cursor()
    c.execute(prepared_statement, (Id,))
    conn.commit()
    c.execute('''  SELECT * FROM COVID19  ''')
    config.data = DataFrame(c.fetchall(), columns=['index', 'pruid', 'prname', 'prnameFR', 'date', 'numconf', 'numprob',
                                                   'numdeaths', 'numtotal', 'numtoday', 'ratetotal'])

def plotPieChart(pieType, pieState, pieDateStart, pieDateEnd):
    """ Will plot a pie chart based on the information provided by the user

           Args:
                pieType: If the pie chart will be Deaths, Cases or Probable cases
                pieState: Which state other than ontario the user wants the plotting
                pieDateStart: start date
                pieDateEnd: end date
           Returns:
               none
        """
    if (pieState.lower() == "c" ):
        pieState = "Canada"
    filteredDF = config.data[(config.data["prname"] == "Ontario") | (config.data["prname"] == pieState.title()) & (config.data["date"] >= pieDateStart) & (config.data["date"] <= pieDateEnd)]
    if(pieType == "c"):
        filteredDF.groupby(['prname']).sum().plot(kind='pie', y='numconf', autopct='%1.0f')
        plt.xlabel('Number of confirmed cases ' + "from " + pieDateStart + " to " + pieDateEnd)
        plt.ylabel('')
    if(pieType == "d"):
        filteredDF.groupby(['prname']).sum().plot(kind='pie', y='numdeaths', autopct='%1.0f')
        plt.xlabel('Number of deaths ' + "from " + pieDateStart + " to " + pieDateEnd)
        plt.ylabel('')
    plt.title("Covid 19")
    plt.show()

    print(filteredDF)
    return

def createNewCsv():
    """ Will create new file with the modified DataFrame

       Args:
           none
       Returns:
           none
    """
    data = config.data
    data.to_csv(config.newFilePath, index=False)

