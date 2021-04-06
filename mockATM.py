import random
from datetime import datetime as dt



date_time= dt.now()
database = {}
currentBalance = 10000


   
#log out of current session   
def logout():
    response = input("would you like to perform another operation? reply with y(yes), or n(no):".lower())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == "no":
        print("Please Take your card and thanks for banking with us.")
        exit()
        
        
#customers makes complaints
def complaint():
    complaint = input("What issue will you like to report?: ")
    print("Your Complaint goes thus: ", complaint)
    print("Thank you for contacting us.")
    response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us")
        exit()

  
#funds withdrawal function
def withdrawal():
    global currentBalance
    withdrawal = int(input("How much would you like to withdraw?: "))
    if withdrawal <= currentBalance:
        currentBalance = currentBalance - withdrawal
        print("Take your cash, your new current balance is ", currentBalance)
    elif  withdrawal > currentBalance:
        print("You dont have enough funds to complete this transactions")
    response = input("Would you like to perform another operation? type y/yes or n/no: \n".casefold())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us, you may take your card")
        exit()
        

# funds deposit function   
def deposit():
    global currentBalance
    deposit = int(input("How much would you like to deposit?: "))
    currentBalance = currentBalance + deposit
    print("you have eposited ", deposit," and your current balance is", currentBalance)
    response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us, you may take your card")
        exit()

   
#selected operations function 
def bankOperation(user):
    print("Welcome", user[0].upper(), user[1].upper(), "you are logged in on :", date_time, "\n")
    print("What operation would you like to perform?")

    selectedOption = int(input("[1] - CASH DEPOSIT.\n[2] - CASH WITHDRAWAL.\n[3] - COMPLAINTS.\n[4] - LOGOUT\n[5] - EXIT\n:"))
    
    if selectedOption == 1:
        deposit()
        
    elif selectedOption == 2:
        withdrawal()
        
    elif selectedOption == 3:
        complaint()
        
    elif selectedOption == 4:
        logout()
        
    elif selectedOption == 5:
        print("Please take your card and thanks for banking with us.")
        exit()
    else:
        print("invalid option selected please try again")
        bankOperation()
        
  
  
#Users login function 
def login():
    print("*** Login into your Account ***")
    
    accountNumberFromUser = int(input("Enter your Account Number: ") )
    password = input("Enter your password: ")
    
    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)       
    print("Invalid Account or Password")
    login()
                
    
    
#Account number generating function  
def generateAccountNumber():
   return random.randrange(1111111111,9999999999)
    
    
# New Users registeration function   
def register():
    print("******* Create an Account *******\n")
    email = input("Enter your email address: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")

    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has Been Created\n")
    print("==== ====== ====== ===== =====")
    print("Your account number is: ", accountNumber)
    print("Make sure you keep it safe.")
    print("==== ====== ====== ===== =====\n")
    login()
 
    
# Start of the applications  function
def init():
    print("Welcome to bankPHP")
    haveAccount = int(input("Do you have an account with us: 1 for (Yes), 2 (No)?: "))
    if haveAccount == 1:
        login()  
        
    elif haveAccount == 2:
        register() 
    else:
        print("invalid selection\n")
        init()
init()
