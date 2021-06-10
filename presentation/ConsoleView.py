"""
A simple console view for user
"""
import pandas as pd
import enum
import sys
#import tabulate to have a better view of tables
from tabulate import tabulate

class ConsoleView(enum.Enum):
    SHOW_ALL_DATA = "a"
    SHOW_ONE = "v"
    INSERT_DATA = "i"
    UPDATE_DATA = "u"
    DELETE_DATA = "d"
    EXIT = "x"

def showMenu():
    exit = False
    response = ""
    while (exit != True):
        response = printMenu()
        defineChoice(response)
        if ( response != "" and response == ConsoleView.EXIT.value ):
            exit = True

def printMenu():
    print("Program By JANIO MENDONCA JUNIOR")
    choice = input("Please enter a option: \n(a) all data\n(v) view one data\n"
    + "(i) insert data\n(u) update data\n(d) delete data\n(x) exit program\n")
    return choice

def readFile():
    """this function will read the .csv file inside the work folder, named covid19-download.csv
    :param no parameters
    """
    # the try/except will catch any problem raised from the trying of open file
    try:
        # a global variable data was defined to be used outside the method readFile()
        global data
        # using pandas usecols is possible to specify exactly which column will be read from file
        data = pd.read_csv("covid19-download.csv",
                       usecols = ['pruid','prname','prnameFR','date','numconf','numprob',
                                  'numdeaths','numtotal','numtoday','ratetotal'])


    #if the file is unavailable or missing the exception will be handled and printed here
    except FileNotFoundError:
        print("JANIO MENDONCA JUNIOR")
        print ("Could not open the file or file not available")
        sys.exit()

def PrintDataset():
    # Reading the values from columns and assigning it to arrays
    pruid = data['pruid'].values
    prname = data['prname'].values
    prnameFR = data['prnameFR'].values
    date = data['date'].values
    numconf = data['numconf'].values
    numprob = data['numprob'].values
    numdeaths = data['numdeaths'].values
    numtotal = data['numtotal'].values
    numtoday = data['numtoday'].values
    ratetotal = data['ratetotal'].values

    # printing the content of array values_pruid after for loop
    print("--------------------------------------")
    print("Values from prname printed within a for loop:")
    print("--------------------------------------")
    # while loop to traverse the array prname with values from column

    # integer value
    i = 0
    print("The data type is: ", type(i));
    while i < 10:
        print(prname[i])
        i = i + 1
    print("--------------------------------------\n")

    # this array was created with columns name for tabular printing
    headers = ['pruid', 'prname', 'prnameFR', 'date', 'numconf',
               'numprob', 'numdeaths', 'numtotal', 'numtoday', 'ratetotal']
    # zip - A zip object yielding tuples until an input is exhausted.
    table = zip(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal)
    print("\n Printing the infromation passed to the arrays variables created")
    print("------------------------------------------------------------------\n")
    # the function tabulate will the itarable itens from table list
    print(tabulate(table, headers=headers))

def defineChoice ( choice ):
    if (choice == ConsoleView.SHOW_ALL_DATA.value):
        print(" option a ")
        #printList()
    if (choice == ConsoleView.SHOW_ONE.value):
        print(" option v ")
        #viewOne()
    if (choice == ConsoleView.INSERT_DATA.value):
        print(" option i")
        #insert()
    if (choice == ConsoleView.UPDATE_DATA.value):
        print(" option u")
        #update()
    if(choice == ConsoleView.DELETE_DATA.value):
        print("option d")
        #delete()a
    if(choice == ConsoleView.EXIT.value):
        print("option x")
        #exit()

def  printList():
    readFile()

def viewOne():
    pass
def insert():
    pass
def update():
    pass
def delete():
    pass

if __name__ == "__main__":
    showMenu()