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

    def insert(self):
        pass

def isNewTable():
    cur = mysql.connection.cursor()

    try:
        #result = cur.execute("SELECT * FROM %s" + )
        cur.close()
    except:
        return True
    else:
        return False
users = Table("users", "name", "username", "email", "password")
