from app import mysql, session

class Table():
    def __init__(self, tableName, *args):
        self.table = tableName
        self.columns = "(%s)" %",".join(args)
        if isNewTable(tableName):
            cur = mysql.connection.cursor()
            cur.execute("CREATE TABLE %s%s" %(self.table, self.columns))
            cur.close()

    def getAll(self):
        pass

    def getOne(self):
        pass

    def deleteOne(self, search, value):
        pass

    def drop(self):
        pass

    def insert(self, *args):
        pass

    #check if table already exists
def isnewtable(tableName):
    cur = mysql.connection.cursor()

    try: #attempt to get data from table
        result = cur.execute("SELECT * from %s" %tableName)
        cur.close()
    except:
        return True
    else:
        return False


