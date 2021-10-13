from classes.data import Data

data = Data()

class Math():

    def getTotals(self):
        print("\nYour current totals are: ")
        data.objToDict(data.getCurrent())
        print("\n")

    def overallTotal(self):
        actualTotal = float(data.getTotal("total")[0])
        print("The overall total is $", actualTotal)
        total = float(0)

        for n in data.getCurrent():
            total += float(n[1])

        print(" and there is $",(actualTotal - (total - actualTotal)),"left\n")



    def deposit(self):
        option = input("Flat = 1 Percentage = 2\n")

        if str(option) == "1":
            name = input("\nWhich account? \n")
            amount = float(input("\nHow much are you depositing? \n"))
            initial = data.getTotal(name)
            final = float(initial[0]) + amount
            data.updateTotal(float(final), name)
            print("\n")


        elif str(option) == "2":
            name = input("\nWhich account? \n")
            split = input("\nHow much do you have? \n")
            percent = input("What percentage do you want to deposit? \n")
            initial = data.getTotal(name)
            final = (float(split) * float(percent)) + initial[0]
            data.updateTotal(float(final),name)
            print("\n")



    def withdraw(self):
        name = input("Which account would you like to withdraw from? \n")
        amount = input("How much are you withdrawing \n")
        initial = data.getTotal(name)
        final = float(initial[0]) - float(amount)
        data.updateTotal(float(final), name)
        print("\n")




    def create(self):
        name = input("What would you like to name your account?\n")
        data.create(name) 
        print("\n")




    def delete(self):
        name = input("Which account do you want to delete? \n")
        check = input("Are you sure? Yes/No \n")

        if check == "Yes" or 'y':
            data.delete(name)
            print("\n")


        else:
            print("Did not delete.")
            print("\n")


