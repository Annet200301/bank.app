import.os

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
def user_details_input():
    name= input("enter the name:")
    address=input("enter the address:")
    nic=input("enter the nic number :")
    email=input("enter the email address:")
    D_O_B=input("enter the date of birth(DD/MM/YYYY):")
    while True:
        try:
            phone_number=int(input("enter the phone number:"))
            break
        except ValueError:
            print("enter a valid phone number!")
    user_id=input("enter the user id:")
    password=input("enter the password:")
    return[name,nic,address,email,D_O_B,phone_number,password,user_id]
customer_details=user_details_input()
print(customer_details)
#==========================id creation======================================================================
def customer_id():
    if not os.path exit ("customer.txt") or os.path.getsize("customer.txt")==0:
        return"C0001"
    with open("customer.txt","r")as file:
        return f"C{int(customers_file.readlines()[-1].split(",")[0][1:]) +1:04}



#============files ===============================================================================================================================================
with  open("customer.txt","a")as file:
    file.write(f"{customer_details[0]},{customer_details[1]},{customer_details[2]},{customer_details[3]},{customer_details[4]},{customer_details[5]}\n")
with  open("user_details","a") as file:
    file.write(f"{customer_details[-1]},{customer_details[-2]}\n")
#================================================================================================================================================================





