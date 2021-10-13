import json
import sqlite3

from passlib.hash import sha256_crypt

from config import Config

config = Config()




class Cat:





    def __init__(self):
        # put properties here

        # path is relative to root of app (app.py)
        self.dbPath = config.dbName



    def sqlConvert(self):

        self.row_factory = sqlite3.Row





    def addNewOwner(self, ownerName, ownerAddress, ownerPhoneNumber, ownerEmail):

        with sqlite3.connect(self.dbPath) as con:

            cur = con.cursor()
            cur.execute("INSERT INTO owner (name, address, phoneNumber, email) VALUES (?,?,?,?)",(ownerName, ownerAddress, ownerPhoneNumber, ownerEmail))
            con.commit()    
            cur.close()

            return True



    def getOwners(self):

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()

            cur.execute("SELECT id, name FROM owner")
            owners = cur.fetchall()
            con.commit()
            cur.close()
 
            if owners:
                return owners
            else:
                return False




    def addNewCat(self, catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate):

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()

            catId = cur.execute("INSERT INTO cat (name, owner, medicationYN, medicationDetails, diet, likesDislikes, behaviourYN, behaviourDetails, other, dateLeaving) VALUES (?,?,?,?,?,?,?,?,?,?)",(catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate)).lastrowid
            con.commit()
            cur.execute("INSERT INTO cat_owner (id_owner, id_cat) VALUES (?,?)",(catOwner,catId))
            con.commit()   
            cur.close()
            
            return True 


    def retrieveAllCats(self):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT *, owner.name AS ownerName FROM cat JOIN owner ON owner.id = cat.owner") # ORDER BY (?) DESC", [sortBy]  cat.*, owner.name AS ownerName, owner.address, owner.phoneNumber, owner.email
            result = cur.fetchall()
            cur.close()

            if result:
                return result
            else:
                return False


    def objToDict(self, obj):

        for item in obj:
            print(tuple(item))





    def retrieveAllOwners(self):

        with sqlite3.connect(self.dbPath) as con:
            
            # con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT id FROM owner")
            ownerIds = cur.fetchall()

            d = {}

            for id in ownerIds:
                
                newId = int(''.join(map(str,id)))
                s = cur.execute("SELECT * FROM owner,cat INNER JOIN cat_owner ON id_cat = cat.id AND id_owner = owner.id WHERE owner.id = ? ",id)
                d[newId] = list(s)
                # a = cur.execute("SELECT * FROM cat WHERE cat.owner = ?",(id)) 
                # print(list(a))
                # print(newId, list(a))
                if d[newId] == []:
                    b = cur.execute('SELECT * FROM owner WHERE id = ?', id)
                    d[newId] = list(b)
        return d





    def retrieveCurrentCats(self):

        with sqlite3.connect(self.dbPath) as con:

            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT cat.*, owner.name AS ownerName, owner.address, owner.phoneNumber, owner.email FROM cat JOIN owner ON owner.id = cat.owner WHERE inCattery = 1") # ORDER BY (?) DESC", [sortBy]
            result = cur.fetchall()
            cur.close()

            if result:
                return result
            else:
                return False




    def deleteCat(self,catId):

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT * FROM cat WHERE id = ?",[catId])
            result = cur.fetchone()

            if result:
                cur.execute("DELETE FROM cat WHERE id = ?",[catId])
                cur.close()
                return True
            else:
                cur.close()
                return False



    def deleteOwner(self,ownerId):

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT * FROM owner WHERE id = ?",[ownerId])
            result = cur.fetchone()

            if result:
                cur.execute("DELETE FROM owner WHERE id = ?",[ownerId])
                cur.close()
                # print("id = ",ownerId,"delete owner result = ",result)
                return True
            else:
                cur.close()
                return False




    def addCat(self,catId):

         with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT inCattery FROM cat WHERE id = ?",[catId])
            result = cur.fetchone()

            if result:
                cur.execute("UPDATE cat SET inCattery = ? WHERE id = ?",[1,catId])
                cur.close()
                return result

            else:
                cur.close()
                return False




    def removeCat(self,catId):

         with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT inCattery FROM cat WHERE id = ?",[catId])
            result = cur.fetchone()

            if result:
                cur.execute("UPDATE cat SET inCattery = ? WHERE id = ?",[0,catId])
                cur.close()
                return result

            else:
                cur.close()
                return False





    def editCat(self,catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate,catId): #ownerName, ownerAddress, ownerPhoneNumber, ownerEmail, 

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT * FROM cat WHERE id = ?",[catId])
            result = cur.fetchone()
            if result:
                cur.execute("UPDATE cat SET name = ?, owner = ?, medicationYN = ?, medicationDetails = ?, diet = ?, likesDislikes = ?, behaviourYN = ?, behaviourDetails = ?, other = ?, dateLeaving = ? WHERE id = ?",[catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate,catId])
                cur.close()
                return result

            else:
                cur.close()
                return False




    def editOwner(self, ownerName, ownerAddress, ownerPhoneNumber, ownerEmail, ownerId):

        with sqlite3.connect(self.dbPath) as con:
            
            cur = con.cursor()
            cur.execute("SELECT * FROM owner WHERE id = ?",[ownerId])
            result = cur.fetchone()
            
            if result:
                cur.execute("UPDATE owner SET name = ?, address = ?, phoneNumber = ?, email = ? WHERE owner.id = ?",[ ownerName, ownerAddress, ownerPhoneNumber, ownerEmail,ownerId])
                cur.close()
                return result

            else:
                cur.close()
                return False




    def retrieveSingleCat(self,catId):

        with sqlite3.connect(self.dbPath) as con:
            
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM cat WHERE id = ?",[catId]) 
            result = cur.fetchone()
            cur.close()

            if result:
                return result
            else:
                return False



    def retrieveSingleOwner(self,ownerId):

        with sqlite3.connect(self.dbPath) as con:
            
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM owner WHERE id = ?",[ownerId]) 
            result = cur.fetchone()
            cur.close()
            if result:
                return result
            else:
                return False
