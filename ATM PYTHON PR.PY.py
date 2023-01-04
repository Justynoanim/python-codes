print("WELCOME TO ACPN MICROFINANACE BANK")
print("Insert your card please")
password=1234
password=int(input("Enter your 4 digit ATM pin "))
if password!= 1234:
    print("incorrect password!")
else: pass
balance=50000
if password==1234:
    while True:
        print("1=Deposit Money")
        print("2=Withdrawal")
        print("3=Tranfer Money")
        print("4=Check Balance")
        print("5=Exit")
        try:
            option=int(input("Choose any option to continue  "))
        except:
            print("Please select  appropriate option above to continue")
        if option==1:
            a = input("Account Number:")
            b= input("Enter the Amount: ")
            print(b)
            print(f" Your account has been credited with {b}")
            print (f" Your Current  Balance is {int(b)+balance}")
            print("THANK YOU FOR BANKING WITH US")
            print("*********************************************")
        if  option== 2:
            c=input("Account Number:")
            d = input("Enter the Amount: ")
            print(f" {d} is debit from your account")
            print(f"your Current balance is  {balance-int(d)}")
            print("THANK YOU FOR BANKING WITH US")
            print("*********************************************")
        if option==3:
            e = input("Account Number:")
            f= input("Enter the Amount you want to transfer: ")
            print(f)
            print(f" your account is credit with {f}")
            print(f"Your Current balance is {balance-int(f)}")
            print("THANK YOU FOR BANKING WITH US")
            print("*********************************************")
        if  option==4:
            print(f" Your current account balance is {balance}")
            print("*********************************************")
        if option==5:
            print("THANK FOR BANKING WITH US")
            print("Do you want to perform another transaction, choose from the options to continue")
            break

