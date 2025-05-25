from app import mysql, session

class Table():
    def __init__(self, tableName, *args):
        self.table = tableName
        self.columns = "(%s)" %",".join(args)
        if isnewtable(tableName):
            cur = mysql.connection.cursor()
            cur.execute("CREATE TABLE %s%s" %(self.table, self.columns))
            cur.close()

    def getAll(self):
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM %s" %self.table)
        data = cur.fetchAll(); return data

    def getOne(self, search, value):
        data = {}
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM %s WHERE %s = \"%s\""  %(self.table, search, value))
        if result > 0: data = cur.fetchone()
        cur.close(); return data

    def deleteOne(self, search, value):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM %s WHERE %s = \"%s\"" %(self.table, search, value))
        mysql.connection.commit(); cur.close

    def drop(self):
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE %s" %(self.table))
        cur.close()

    def insert(self, *args):
        cur = mysql.connection.cursor()
        data = ""
        for arg in args:
            data += "\"%s\"," %(arg)
        cur.execute("INSERT INTO %s%s VALUES(%s)" %(self.table, self.columns, data[:len(data) -1]))
        mysql.connection.commit()
        cur.close()


def sql_raw(execution):
    cur = mysql.connection.cursor()
    cur.execute(execution)
    mysql.connection.commit()
    cur.close()

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

def isNewUser():
    users = Table("users", "name", "email", "username", "password")
    data = users.getAll()
    usernames = [user.get('username') for user in data]

    return False if username in usernames else True


