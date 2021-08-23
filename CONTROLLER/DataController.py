"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 25/06/2021
Version: 2.0

This file is responsible to make the CONTROLLER part of MVC. The controller is the middle man between the MODEL and VIEW.
the CONTROLLER get information from VIEW, pass it to MODEL and reply MODEL back.
"""
from MODEL import DataModel



def getOneRow(RowId):
    """ Will call the function getOneRow() from MODEL layer

        Args:
            RowId: the row Id supplied by the user
        Returns:
            none
    """
    row = DataModel.getOneRow(RowId)
    return row

def getManyRows(RowNumbers):
    """ Will call the function getManyRows() from MODEL layer

        Args:
            RowNumbers: the with the rows Id's supplied by the user
        Returns:
            none
    """
    rows = DataModel.getManyRows(RowNumbers)
    return rows

def insert(Row):
    """ Will call the function insert() from MODEL layer

        Args:
            Row: the row to be inserted
        Returns:
            none
    """
    DataModel.insertData(Row)

def update(Id, Row):
    """ Will call the function update() from MODEL layer

        Args:
            Row: the row to be inserted
        Returns:
            none
    """
    DataModel.updateData(Id, Row)

def delete(Id):
    """ Will call the function delete() from MODEL layer

            Args:
                Id: the row Id to be deleted
            Returns:
                none
    """
    DataModel.deleteData(Id)

def plotPieChart(pieType, pieState, pieDateStart, pieDateEnd):
    """ Will call the function plotPieChart from MODEL layer

                Args:
                    pieType: If the pie chart will be Deaths, Cases or Probable cases
                    pieState: Which state other than ontario the user wants the plotting
                    pieDateStart: start date
                    pieDateEnd: end date
                Returns:
                    none
        """
    DataModel.plotPieChart(pieType, pieState, pieDateStart, pieDateEnd)

def createNewCsv():
    """ Will call the function createNewCsv() from MODEL layer
            Args:
                none
            Returns:
                none
    """
    DataModel.createNewCsv()

