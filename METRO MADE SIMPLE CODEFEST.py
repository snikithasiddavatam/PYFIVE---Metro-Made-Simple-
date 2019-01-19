#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Booking a ticket
import random
names=[]
ages=[]
genders=[]
pnr=[]
transactionDetails=[]
balance=1000
y=100000
phoneNumber=9666697782
aadharNumber=121234345656
paytm_otp=123456
print("Welcome to Metro Made Simple!")
username=input("Username: ")
password=input("Password: ")
if username=='123' and password=='1234':
    print("You have successfully logged in!")
    while(True):
        menu=input("Enter 1 - Booking a ticket \nEnter 2 - Timings of Metro \nEnter 3 - Recharge my metro card \nEnter 4 - Lost my metro card \nEnter 5 - Check my balance \nEnter 6 - About Metro \nEnter 7 - Show Tickets \nEnter 8 - Purchase a Gift card \nEnter 9 - Transaction History \nEnter 10 - Exit: \n")
        if menu=='1':
            print("BOOKING A TICKET")
            c=input("From: ")
            d=input("To: ")
            b=int(input("Enter the number of seats: "))
            for x in range(1,b+1):
                name=input("Name: ")
                names.insert(x,name)
                age=input("Age: ")
                ages.insert(x,age)
                gender=input("Gender: ")
                genders.insert(x,gender)
                pnr.insert(x,y)
            print("These are the details you have entered: ")
            for x in range(0,b):
                print(names[x])
                print(ages[x])
                print(genders[x])
            print("Your PNR Number: ",y);
            y=y+1;
            cost=50*b
            transactionDetails.append(-1*cost)
            print("Total cost of Tickets: ",cost)
            balance = balance - cost
            print("Updated balance: "+str(balance))
            print("The token(OTP) for the ticket(s) is: "+str(random.randint(200000,2000000)))
            print("This OTP is valid for one hour only.")
        elif menu=='3':
            recharge = int(input("Enter the recharge amount: Rs."))
            if recharge<100:
                print ("Insufficient amount to recharge!")
            elif recharge>100:
                pay = int(input("Enter the paytm number: "))
                count = 0
                while(pay>0):
                    pay = pay // 10
                    count = count + 1
                    if count == 10:
                        otp=int(input("Enter OTP: "))
                        if otp==paytm_otp:
                            balance = balance + recharge
                            print ("Updated balance: ",str(balance))
        elif menu=='10':
            break;
else:
    print("Incorrect!")
        
             


# In[ ]:





# In[ ]:




