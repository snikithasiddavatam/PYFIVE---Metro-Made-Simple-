#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Metro Made Simple
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
        elif menu=='2':
            print("TIMINGS OF METRO")
            print('Enter the numbers respectively alloted for each station to get your needed station timing') 
            n=int(input('Enter 1 - A \nEnter 2 - B \nEnter 3 - C \nEnter 4 - D \nEnter 5 - E \nEnter 6 - F \nStation: '))
            if n==1:
                print("THE TIMINGS OF STATION A: ")
                print("6:35 AM \n6:45 AM \n6:55 AM \n7:05 AM \nIn every 10 minutes, train is available till 10:30 PM")
            elif n==2:
                print("THE TIMINGS OF STATION B: ")
                print("6:30 AM \n6:40 AM \n6:50 AM \n7:00 AM \nIn every 10 minutes, train is available till 10:30 PM")
            elif n==3:
                print("THE TIMINGS OF STATION C: ")
                print("6:33 AM \n6:43 AM \n6:53 AM \n7:03 AM \nIn every 10 minutes, train is available till 10:30 PM")
            elif n==4:
                print("THE TIMINGS OF STATION D: ")
                print("6:36 AM \n6:46 AM \n6:56 AM \n7:06 AM \nIn every 10 minutes, train is available till 10:30 PM")
            elif n==5:
                print("THE TIMINGS OF STATION E: ")
                print("6:12 AM \n6:22 AM \n6:32 AM \n6:42 AM \nIn every 10 minutes, train is available till 10:30 PM")
            elif n==6:
                print("THE TIMINGS OF STATION F: ")
                print("6:35 AM \n6:45 AM \n6:55 AM \n7:05 AM \nIn every 10 minutes, train is available till 10:30 PM")
        
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
        elif menu=='4':
            mobileNumber = int(input('Enter the mobile number: '))
            if(mobileNumber == phoneNumber):
                aadhar = int(input('Enter the aadhar number: '))
                if(aadhar == aadharNumber):
                    import random
                    print("Your OTP: ",random.randint(100000,1000000))
                    print("This is valid for one hour only")
                else:
                    print("Please try Again!!! The aadharNumber is incorrect")
            else:
                print("Please try Again!!! The mobileNumber is incorrect")
        elif menu=='5':
            print("Your wallet balance is",str(balance))
        elif menu=='6':
            print("ABOUT METRO:\n\n")
            print("1. Hyderabad Metro Rail(HMR)has been regarded as India's largest metro project. It is the world's largest Public Private Partnership(PPP)under metro sector,stretches over seventy two kilometers around the city.\n")
            print("2. This project was initiated to reduce hyderabads traffic congestion,and pollution.\n")
            print("3. This ambisious project was approved on 4th September,2010 by Government Of Andhra Pradesh.\n")
            print("4. This project was awarded to Larsen & Toubro also known as L&T. \n")
            print("5. If the citizens of Hyderabad adopt metro then approximately 1.5 to 2 lakh tons of carbon can be saved from being released into the environment.\n")
            print("6. This project has been given the title L&T HMRL: LARSEN AND TOUBRO HYDERABAD METRO RAIL LIMITED \n\n")  
            print("ADVANTAGES OF HMR \n\n ")
            print("1. High capacity carriers \n")
            print("2. Low energy consumption \n")
            print("3. Greater traffic carrying capacity. \n")
            print("4. Low ground space occupation. \n")
            print("5. Eco friendly \n\n")
            print("HIGHLIGHTS OF HMR \n\n")
            print("1. World class stations. \n")
            print("2. Automatic fare collection and ticket vending machines.\n")
            print("3. Ultra modern coaches.\n")
            print("4. High frequency of trains reducing waiting time.\n")
            print("5. User friendly stations.\n")
            print("6. Connects major offices,retail and residentail areas.\n\n")
            print("CORRIDORS OF HMR \n\n")
            print("The hyderabad metro has three corridors.\n")
            print("CORRIDOR 1 : MIYAPUR TO LB NAGAR.  STOPS: 27 . LENGTHS : 28.87 KM. \n")
            print("CORRIDOR 2 : JBS(Jubliee Bus Station) TO FALAKNUMA. STOPS : 16 . LENGTH : 14.78 KM \n ")
            print("CORRIDOR 3 : NAGOLE TO SHILPARAMA. STOPS : 23 . LENGTH : 23.51 KM \n\n")
            print("MAINTANANCE OF HMR \n\n")
            print("The Hyderabad has 3 depots MIYAPUR,FALAKNUMA AND UPPAL for the three corridors which have perfect maintenance facilities for the perfect maintenance. \n\n")
            print("FACILITIES OF HMR DEPOTS : \n\n")
            print("1. Automatic train wash plant. \n ")
            print("2. Electronic work shop bays. \n")
            print("3. Depot control center.\n")
            print("4. Stabbling bays. \n")
            print("5. Wheel allignment bays. \n")
            print("6. Engneering and re-work bays. \n")
            print("7. Cafetaria, and confrence rooms.\n \n")
            print("AWARDS AND HONOURS OF HMR: \n\n")
            print("1. BEST METRO RAIL PROJECT OF INDIA (2013 & 14).\n")
            print("2. ROYAL SOCIETY AWARD FOR ACCIDENT PREVENTION(2013).\n")
            print("3. GLOBAL ENGENEERING PROJECT OF THE YEAR (2013).\n")
            print("4. BEST TRANSPORTATION PROJECT OF INDIA (2016).\n")
            print("5. BEST UPCOMING METRO RAIL PROJECT (2015 & 17 )\n")
            print("SAFTEY  AND SECURITY OF HMR  \n\n")
            print("1. CCTV and intrusion detection systems across Metro premises are continuously monitored.\n")
            print("2. Dedicated security staff equipped with communication system. \n")
            print("3. Centralized access control. \n\n")
            print("COMPARISION OF METRO WITH ROAD TRANSPORT \n\n")
            print("METRO: \n\n")
            print("1. They are fast in terms of movement and speed.")
            print("2. Low carbon emission.")
            print("3. It has more efficiency as it is big in size.")
            print("4. Costs more due facilities. \n\n")
            print("ROAD TRASPORT \n\n")
            print("1. Moves slowly due to traffic.")
            print("2. High carbon emision.")
            print("3. Low effiency as it is small in size. ")
            print("4. Costs less as there less facilities. \n\n ")
            print("FREQUENTLY ASKED QUESTIONS(FAQ'S) \n\n")
            print("Q1. Why do we need metro in Hyderabad ? \n\n")
            print("ANS : With almost 8 million inhabitants in Hyderabad, traffic mobility is one of the most important issues. Hyderabad Metro Rail will to reduce traffic jams and pollution . \n\n")
            print("Q2. What makes Hyderabad  metro unique in India ? \n\n")  
            print("ANS : Hyderabad Metro Rail (HMR) is the largest public private partnership (PPP) project in the world in the Metro rail category which makes it unique. \n\n ")
            print("Q3. How will hyderabad metro improve my travelling experience ? \n\n")
            print("ANS : Hyderabad Metro will provide end to end connectivity to passengers. \n\n")
            print("Q3. What are the fecilities provided in metro stations ? \n\n")
            print("ANS :  All metro stations will have designated shopping and dining areas where you can shop for your daily needs and also enjoy a hearty meal with family and friends. Each station has staircases, elevators and escalators for the convenience of passengers. \n\n")
            print("Q4. Can passengers bring eatables into metro stations/trains? \n\n")
            print("ANS : No,the passengers are not allowed to carry any eatables. \n\n")
            print("MY CITY")
            print("MY METRO")
            print("MY PRIDE")
        elif menu=='10':
            break;
else:
    print("Incorrect!")
        
             


# In[ ]:





# In[ ]:




