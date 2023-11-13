import random

#Python Skills Check -- Jonathan Wells

#Helper functions

def incomeTax():
    """This function takes the users input, checks to see if it's a valid number, and if it is,
    returns the input x.04"""
    #None -> Number
    print("Welcome to the income tax calculator")
    while True:
        income = input("Enter your income for this year (Without commas): ")
        try:
            income = float(income)
            break
        except:
            print("Please enter a valid amount")
    return income *.04

def username(fName, lName):
    """This function takes the users first and last name, and returns a username with those two names"""
    #String, String -> String
    return fName[0:3] +lName[0:4]

def password(wordList):
    """This function takes a list of words, and picks a random word, as a well as a number between 10-100
    to create a password"""
    #List -> String
    word = random.choice(wordList)
    return word + str(random.randint(10,100))


#######    Body
randomList = ["Camping", "Entry", "Engine", "Shop", "Market", "Jacket", "Taiga", "Mouse"]

print("Welcome to Tom Nook's store management program!")
print("2021 Jonathan Wells for Nook Industries")
print("-----------------------------")

print("Select one of the following options: ")
print("[A]: Income tax calculator")
print("[B]: Create an employee account")
print("[C]: End this program")

userInput = input("Please type in A, B, or C: ")
while userInput != "A" and userInput != "B" and userInput != "C":
    print("Invalid input!")
    userInput = input("Please type in A, B, or C: ")

if userInput != "C":
    if userInput == "A":
        print("Expect to pay around $" + str(incomeTax()) + " in taxes this year.")
    elif userInput == "B":
        print("Welcome to the username and password generator.")
        firstName = input("Please enter the employee's first name: ")
        print("Thank you")
        lastName = input("Please enter the employee's last/sur name: ")
        print("Thank you")
        userN = username(firstName, lastName)
        passW = password(randomList)
        print("")
        print("The employee's username will be " + userN)
        print("")
        print("The employee's temporary password will be " + passW)

print("")
print("")
print("Done")
        
