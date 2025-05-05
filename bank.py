#========================================================
def staff_menu():
    print("===============MENU OPTION===============")
    print("1:New customer creation")
    print("2:New cutomer account creation")
    print("3:Account details")
    print("3:Deposit")
    print("4:Withdrawel")
    print("5:Check balance")
    print("6:Transaction history")
    print("7:Staff details")
    print("7:Exit")
#========================================================
def  customer_menu():
    print("===============MENU OPTION===============")
    print("1:Deposit")
    print("2:Withdrawel")
    print("3:Check balance")
    print("4:Transaction history")
    print("5:Exit")
#=====amount function=======================================================================================
def validation_of_amount():
    while True:
        try:
            Amount= int (input("enter the amount:"))
            if Amount>0:
                break
        except ValueError:
            print ("your balance is invalid")
#=============================================================================================================
def option():
    while True:
        try:
            option=int(input("enter the option you choose:"))
            break
        except ValueError:
            print(" your choosed option is invalid")
#===========================================================================================================
def option_progress():







#===========================================================================================================
print("==========login==========")
print("Welcome! there,for system protection ,you have to go through the following process")
print("initial_user_id=Authority01,initial_password= 08052025A1")
print("\n")
initial_user_id="Authority01"
initial_password= "08052025A1"
while True:   
    Initial_id= input("Enter the ID  here, if you are the recognited authoritative:")
    if Initial_id==initial_user_id:
        Initial_pass=input("Enter the PASSWORD here:")
        if Initial_pass==initial_password:
            print("Now you can  use the system for your need")
            option()
            break
        else:
            print("your Initial_pass is WRONG , please re-enter the initial_pass correctly below")
    else:
        print("your Initial_id is wrong.print the correct ID which is given by the sytem developer ")
#sytem login as staff or customer=============================================================================
        