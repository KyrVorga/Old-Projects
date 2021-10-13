import sqlite3


class Data:

    def __init__(self):
        
        self.dbPath = "database/database.db"

    def sqlConvert(self):

        self.row_factory = sqlite3.Row

    def objToDict(self, obj):

        for item in obj:
            print(tuple(item))



    def getCurrent(self):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT name, total FROM accounts")
            result = cur.fetchall()
            cur.close()
            return result

    def getRates(self):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT percent FROM accounts")
            result = cur.fetchall()
            cur.close()
            return result



    def getTotal(self, name):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT total FROM accounts WHERE name=?",[name])
            result = cur.fetchone()
            cur.close()
            return result



    def updateTotal(self, amount, name):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("UPDATE accounts SET total=? WHERE name=?",[amount, name])
            con.commit()
            cur.close()


    def create(self, accountName):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("INSERT INTO accounts (name) VALUES (?)",[accountName])
            con.commit()
            cur.close()



    def delete(self, accountName):

        with sqlite3.connect(self.dbPath) as con:

            cur = con.cursor()
            cur.execute("SELECT * FROM accounts WHERE name = ?",[accountName])
            result = cur.fetchone()

            if result:
                cur.execute("DELETE FROM accounts WHERE name = ?",[accountName])
                con.commit()
                cur.close()
                return True
            else:
                cur.close()
                return False


    # def addNewOwner(self, ownerName, ownerAddress, ownerPhoneNumber, ownerEmail):

    #     with sqlite3.connect(self.dbPath) as con:

    #         cur = con.cursor()
    #         cur.execute("INSERT INTO owner (name, address, phoneNumber, email) VALUES (?,?,?,?)",(ownerName, ownerAddress, ownerPhoneNumber, ownerEmail))
    #         con.commit()    
    #         cur.close()

    #         return True



    # def retrieveAllCats(self):

    #     with sqlite3.connect(self.dbPath) as con:

    #         con.row_factory = sqlite3.Row
    #         cur = con.cursor()
    #         cur.execute("SELECT *, owner.name AS ownerName FROM cat JOIN owner ON owner.id = cat.owner") # ORDER BY (?) DESC", [sortBy]  cat.*, owner.name AS ownerName, owner.address, owner.phoneNumber, owner.email
    #         result = cur.fetchall()
    #         cur.close()

    #         if result:
    #             return result
    #         else:
    #             return False