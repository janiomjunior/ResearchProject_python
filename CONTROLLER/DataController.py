from MODEL import DataModel

def getOneRow(RowId):
    row = DataModel.getOneRow(RowId)
    return row

def getManyRows(RowNumbers):
    rows = DataModel.getManyRows(RowNumbers)
    return rows

def insert(Row):
    DataModel.insertData(Row)

def update(Id, Row):
    DataModel.updateData(Id, Row)

def delete(Id):
    DataModel.deleteData(Id)

def createNewCsv():
    DataModel.createNewCsv()

