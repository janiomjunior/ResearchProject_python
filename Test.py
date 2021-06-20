"""
Author: Janio Mendonca Junior
Course: CST8334 - Spring2021
Date: 25/06/2021
Version: 1.0
"""
import unittest
import config
from MODEL import DataModel
import pandas.api.types as ptypes

global df1
global df2

class Test(unittest.TestCase):

#this module test will check if the parsing was correctly made by checking the if the data is placed
#on the correct column data type
#Actually will check if the data in memory has 100 rows
    def test_parsing(self):
        config.data = DataModel.readFile(config.filePath)
        cols_to_check_num = ['pruid','numtoday','numprob','numdeaths','numtotal','numtoday','ratetotal']
        # will cehck if the columns from cols_to_check_num are numeric type
        assert all(ptypes.is_numeric_dtype(config.data[col]) for col in cols_to_check_num)
        # will cehck if the columns from cols_to_check_string are numeric type
        cols_to_check_string = ['prname', 'prnameFR','date']
        assert all(ptypes.is_string_dtype(config.data[col]) for col in cols_to_check_string)
        #Will check if the size parsed is the specified for 100 rows
        self.assertEqual(100, len(config.data))

#this module will check if the function inseertData defined on MODULE will correctly insert data at the
#end of the data parsed in memory. The module will do it by comparing the data frame size by reading at
#first time and by inserting a new row.
    def test_insertData(self):
        row = {'pruid': 11, 'prname': 'TestUnit', 'prnameFR': 'TestUnit', 'date': '1111-11-11', 'numconf': 11, 'numprob': 11,
               'numdeaths': 11, 'numtotal': 11, 'numtoday': 11, 'ratetotal': 11}
        config.data = DataModel.readFile(config.filePath)
        df1 = len(config.data)
        DataModel.insertData(row)
        df2 = len(config.data)
        self.assertNotEqual(df1, df2)
        # pruid_lastValue = config.data.pruid[len(config.data)-1]
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

#this module will check if the the function updateData() from MODEL, properly update the row index 5,
#by checking the data before run the function and after run the updateData().
    def test_updateData(self):
        row = [11, 'TestUnit', 'TestUnit', '1111-11-11', 11, 11, 11, 11, 11, 11]
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

#This module will check if the size of the data parsed in memory has one position lees after
#run the function deleteData from DataModel.
    def test_deleteData(self):
        config.data = DataModel.readFile(config.filePath)
        df1 = len(config.data)
        DataModel.deleteData(5)
        df2 = len(config.data)
        self.assertNotEqual(df1, df2)

#this module will check if the the function readFile(filePath) from DataModel will porperly raise a
#exception when the file path is wrong
    def test_readFileTryCatch(self):
        filePath = "/Users/janiomjunior/pythonProject/Assignment_2/covid19.csv"
        self.assertRaises(TypeError, DataModel.readFile(filePath))

if __name__ == '__main__':
    unittest.main()