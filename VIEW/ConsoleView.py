"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 25/06/2021
Version: 2.0

This file is responsible for all the user iterations and compose the VIEW layer of MVC pattern.
"""

import enum
import re
from datetime import datetime

from MODEL import DataModel
from CONTROLLER import DataController
import config

class ConsoleView(enum.Enum) :
    '''
    "a" value for option SHOW_ALL
    "v" value for option SHOW_ONE
    "m" value for option SHOW_MANY
    "i" 'value for option INSERT
    "u" value for option update
    "d" value for option delete
    "n" value for new file
    "x" value for exit value
    '''

    SHOW_ALL_DATA = "a"
    SHOW_ONE = "v"
    SHOW_MANY = "m"
    INSERT_DATA = "i"
    UPDATE_DATA = "u"
    DELETE_DATA = "d"
    NEW_FILE = "n"
    EXIT = "x"

def showMenu():
    """Call the menu options and step out the program

    Args:
        none
    Returns:
        None
    """

    exit = False
    response = ""
    while (exit != True):
        response = printMenu()
        defineChoice(response)
        if ( response != "" and response == ConsoleView.EXIT.value ):
            print("ByeBye!")
            exit = True

def printMenu():
    """shows the menu options

        Args:
            none
        Returns:
            choice: the character selected
    """
    print("Program By JANIO MENDONCA JUNIOR")
    choice = input("Please enter a option: \n(a) view all data\n(v) view one data\n"
    + "(m) view multiples\n(i) insert data\n(u) update data\n(d) delete data\n(n) Create a new .csv file\n(x) exit program\n: ")
    return choice

def printDataset():
    """Print the entire dataset parsed

        Args:
            none
        Returns:
            none
    """
    print(config.data.head(105))

def viewOne():
    """show just one row of dataset in memory

        Args:
            none
        Returns:
            none
    """
    Id = input("Please enter the row ID: ")
    print("--------")
    print(DataController.getOneRow(Id))
    print("--------")

def viewMany():
    """show multiples rows based on user input

        Args:
            none
        Returns:
            none
        """
    #the user will input many row to be printed
    inputRow = input("please enter with the row ID's ex: 2, 3, 5, 6, 7: ")
    #the program will find only numbers from the string input and create a list of numbers to be passed
    rowNumbers = re.findall(r'[\d.]+', inputRow)
    for i in range(0, len(rowNumbers)):
        rowNumbers[i] = int(rowNumbers[i])
    print("--------")
    print(DataController.getManyRows(rowNumbers))
    print("--------")

def dateValidation(date_input):
    """ will validate the date from user input

        Args:
            date_input: date entered by user
        Returns:
            True: for a valid format YYYY-MM-DD
            False: for a invalid format
    """
    format = "%Y-%m-%d"
    try:
        datetime.strptime(date_input, format)
        return True
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return False

def intOrStringValidation(data_input):
    """ will validate the data input from user
        Args:
            data_input: number or string entered by user
        Returns:
            True: for a number format
            False: for a string format
    """
    #will check ig the input is a number
    if data_input.strip().isdigit():
        return True
    #will return false in case of a number
    else:
        return False

def inputNumberChecking (Validation):
    """ will be asking for a validate number
                            Args:
                                data_input: input from user
                            Returns:
                                none
    """
    while Validation==False:
        user_input = input("INVALID input.....Enter a number: ")
        Validation = intOrStringValidation(user_input)

    return

def inputStringChecking (Validation):
    """ will be asking for a validate string
                                Args:
                                    data_input: input from user
                                Returns:
                                    none
    """

    while Validation==True:
        user_input = input("INVALID input.....Enter a String: ")
        Validation = intOrStringValidation(user_input)

    return

def ColumnValues():
    """ Will be storing the inputs from user in properly arrays
                                Args:
                                    none
                                Returns:
                                    none
        """
    global pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal

    #Error checking implemented for the inputs

    print("--------------------")
    pruid_input = input("Enter with the PRUID: ")
    inputNumberChecking(intOrStringValidation(pruid_input))
    pruid = pruid_input

    prname_input = input("Enter with the prname: ")
    inputStringChecking(intOrStringValidation(prname_input))
    prname = prname_input

    prnameFR_input = input("Enter with the prnameFR: ")
    inputStringChecking(intOrStringValidation(prnameFR_input))
    prnameFR = prnameFR_input

    date_input = input("Enter with the date (YYYY-MM-DD): ")
    while dateValidation(date_input) == False:
        user_input = input("INVALID date....Enter a valid Date: ")
        dateValidation(user_input)
        date_input = user_input
    date = date_input

    numconf_input = input("Enter with the numconf: ")
    inputNumberChecking(intOrStringValidation(numconf_input))
    numconf = numconf_input

    numprob_input = input("Enter with the numprob: ")
    inputNumberChecking(intOrStringValidation(numprob_input))
    numprob = numprob_input

    numdeaths_input = input("Enter with the numdeaths: ")
    inputNumberChecking(intOrStringValidation(numdeaths_input))
    numdeaths = numdeaths_input

    numtotal_input = input("Enter with the numtotal: ")
    inputNumberChecking(intOrStringValidation(numtotal_input))
    numtotal = numtotal_input

    numtoday_input = input("Enter with the numtoday: ")
    inputNumberChecking(intOrStringValidation(numtoday_input))
    numtoday = numtoday_input

    ratetotal_input = input("Enter with the ratetotal: ")
    inputNumberChecking(intOrStringValidation(ratetotal_input))
    ratetotal = ratetotal_input
    print("--------------------")

def askId() -> int:
    """ will be asking for ID input
        Args:
            data_input: Id entered by the user
        Returns:
            Id: computed Id
    """
    exists = False
    while exists == False:
        Id = input("Please enter a Valid row ID: ")
        #will check if there is the Id on memory DataFrame
        exists = int(Id) in config.data.index
        if exists:
            print("The Line " + Id + ":")
            print("--------------------")
            print(DataController.getOneRow(Id))
            print("--------------------")
            return Id
        else:
            print("Invalid Index")


def insert():
    """ will call the function insert from CONTROLLER.DataController and pass a row to be inserted
            Args:
                none
            Returns:
                none
    """
    ColumnValues()
    row = {'pruid': pruid, 'prname': prname, 'prnameFR': prnameFR, 'date': date, 'numconf': numconf, 'numprob': numprob,
            'numdeaths': numdeaths, 'numtotal': numtotal, 'numtoday': numtoday, 'ratetotal': ratetotal}

    DataController.insert(row)
    # new row created as data dictionary
    print("The new row was added to the DataFrame")
    print(row)

def update():
    """ will call the function insert from CONTROLLER.DataController and pass a row to be inserted
                Args:
                    none
                Returns:
                    none
    """
    index = askId()
    ColumnValues()
    row = [pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal]

    # will call the method update from layer CONTROLLER
    # the array will be passed to the function for update the values.
    DataController.update(index, row)
    print("Row " + index + " Was Updated")

def delete():
    """ will call the function delete from CONTROLLER.DataController and pass a Id to be deleted
                    Args:
                        none
                    Returns:
                        none
    """
    index = askId()
    DataController.delete(index)
    print("Row " + index + " Was Deleted")
    print("--------------------")

def createNewCsv():
    """ will call the function createNewCsv from CONTROLLER.DataController
                        Args:
                            none
                        Returns:
                            none
    """
    DataController.createNewCsv()
    print("the new CSV was created! ")

def initDataFrame(filePath):
    """ this function will load the .csv in memory DataFrame
                            Args:
                                none
                            Returns:
                                none
    """
    config.data = DataModel.readFile(filePath)

#
def defineChoice ( choice ):
    """ Will define the method to be called depending on the user choice
                                Args:
                                    none
                                Returns:
                                    none
    """
    if (choice == ConsoleView.SHOW_ALL_DATA.value):
        print(" option a ")
        printDataset()
    if (choice == ConsoleView.SHOW_ONE.value):
        print(" option v ")
        viewOne()
    if (choice == ConsoleView.SHOW_MANY.value):
        print(" option m ")
        viewMany()
    if (choice == ConsoleView.INSERT_DATA.value):
        print(" option i")
        insert()
    if (choice == ConsoleView.UPDATE_DATA.value):
        print(" option u")
        update()
    if(choice == ConsoleView.DELETE_DATA.value):
        print("option d")
        delete()
    if(choice == ConsoleView.NEW_FILE.value):
        createNewCsv()
        print("option n")


if __name__ == "__main__":
    initDataFrame(config.filePath)
    showMenu()