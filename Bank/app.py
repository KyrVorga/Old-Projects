from classes.data import Data
from classes.math import Math

math = Math()
data = Data()


if __name__ == "__main__":

    flag = True
    print("\n\n\nThis is a psuedo bank manager, what do you need? \n\n\nCurrent totals - 1 \nDeposit - 2 \nWithdraw - 3 \nCreate account - 4 \nDelete account - 5 \nOverall total \nQuit - 7 \n")
    while flag == True:
        choice = input()

        if choice == "1":
            math.getTotals()

        elif choice == "2":
            math.deposit()

        elif choice == "3":
            math.withdraw()

        elif choice == "4":
            math.create()

        elif choice == "5":
            math.delete()

        elif choice == "6":
            math.overallTotal()

        else:
            quit()
else:
    print("Fail")