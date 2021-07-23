"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 25/06/2021
Assignment 3
Version: 3.0
"""
import unittest
import config
from MODEL import DataModel
import pandas.api.types as ptypes

global df1
global df2

class Test(unittest.TestCase):
    """
        this module test will check if the parsing was correctly made by checking the if the data is placed
        on the correct column data type
        Actually will check if the data in memory has 100 rows

        Parameters: a calling to the unittest.TestCase

    """

    def test_insertData(self):
        """
            this module will check if the function insertData defined on MODEL layer will correctly insert data at the
            database. The module will do it by comparing the data frame size. Will read
            the COVID19 table size first, after insert a new row and check each column to see if the properly data was
            inserted

            :return: none
        """
        row = {'pruid': 11, 'prname': 'TestUnit', 'prnameFR': 'TestUnit', 'date': '1111-11-11', 'numconf': 11, 'numprob': 11,
               'numdeaths': 11, 'numtotal': 11, 'numtoday': 11, 'ratetotal': 11}
        DataModel.readFile(config.filePath)
        df1 = len(config.data)
        DataModel.insertData(row)
        df2 = len(config.data)
        self.assertNotEqual(df1, df2)
        self.assertEqual(config.data.pruid[len(config.data)-1], 11)
        self.assertEqual(config.data.prname[len(config.data)-1], 'TestUnit')
        self.assertEqual(config.data.prnameFR[len(config.data)-1], 'TestUnit')
        self.assertEqual(config.data.date[len(config.data)-1], '1111-11-11')
        self.assertEqual(config.data.numconf[len(config.data)-1], 11)
        self.assertEqual(config.data.numprob[len(config.data)-1], 11)
        self.assertEqual(config.data.numdeaths[len(config.data)-1], 11)
        self.assertEqual(config.data.numtotal[len(config.data)-1], 11)
        self.assertEqual(config.data.numtoday[len(config.data)-1], 11)
        self.assertEqual(config.data.ratetotal[len(config.data)-1], 11)

    def test_updateData(self):
        """
            this module will check if the  function updateData() from MODEL layer, properly update the row index 5
            on the database side by checking the data before run the function and after run the updateData().

            :return: none
        """
        row = {'pruid': 11, 'prname': 'TestUnit', 'prnameFR': 'TestUnit', 'date': '1111-11-11', 'numconf': 11,
               'numprob': 11, 'numdeaths': 11, 'numtotal': 11, 'numtoday': 11, 'ratetotal': 11}
        df1 = config.data.iloc[[5]]
        self.assertNotEqual(config.data.pruid[5], 11)
        self.assertNotEqual(config.data.prname[5], 'TestUnit')
        self.assertNotEqual(config.data.prnameFR[5], 'TestUnit')
        self.assertNotEqual(config.data.date[5], '1111-11-11')
        self.assertNotEqual(config.data.numconf[5], 11)
        self.assertNotEqual(config.data.numprob[5], 11)
        self.assertNotEqual(config.data.numdeaths[5], 11)
        self.assertNotEqual(config.data.numtotal[5], 11)
        self.assertNotEqual(config.data.numtoday[5], 11)
        self.assertNotEqual(config.data.ratetotal[5], 11)
        DataModel.updateData(5,row)
        self.assertEqual(config.data.pruid[5], 11)
        self.assertEqual(config.data.prname[5], 'TestUnit')
        self.assertEqual(config.data.prnameFR[5], 'TestUnit')
        self.assertEqual(config.data.date[5], '1111-11-11')
        self.assertEqual(config.data.numconf[5], 11)
        self.assertEqual(config.data.numprob[5], 11)
        self.assertEqual(config.data.numdeaths[5], 11)
        self.assertEqual(config.data.numtotal[5], 11)
        self.assertEqual(config.data.numtoday[5], 11)
        self.assertEqual(config.data.ratetotal[5], 11)

    def test_deleteData(self):
        """
            This module will check if the size of the data persisted in the database has one position less after
            run the function deleteData from DataModel.

            :return: none
        """
        DataModel.readFile(config.filePath)
        df1 = len(config.data)
        DataModel.deleteData(5)
        df2 = len(config.data)
        self.assertNotEqual(df1, df2)

    def test_readFileTryCatch(self):
        """
            this module will check if the the function readFile(filePath) from DataModel will porperly raise a
            exception when the file path is wrong

            :return: none
        """
        filePath = "/Users/janiomjunior/pythonProject/Assignment_2/covid19.csv"
        self.assertRaises(TypeError, DataModel.readFile(filePath))

if __name__ == '__main__':
    unittest.main()