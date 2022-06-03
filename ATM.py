pin={
    1234:"kunal",
    2022:"addy",
    2023:"karan",
    2024:"shubhankar",
    2006:"JIYA"
}
balance={
    "kunal":20000,
    "addy":150,
    "karan":30000,
    "shubhankar":25000,
    "JIYA":42357
    

}




print("****************************************************************************")
print("*                                                                          *")
print("*                           Welcome to  ATM                                *")
print("*                                                                          *")
print("****************************************************************************")
x=int(input("Enter your pin :"))
if x in pin:
       print()
else:
    print("Incorrect pin!!!!!!!!")
for i in pin.keys():
    if x==i:
        print("Welcome",pin[i])
    
        y=pin[i]
bal=(balance[y])
    

print("Press 1-Withdraw")
print("Press 2-Balance Enquiry")
print("Press 3-Fast Cash")
print("Press 4-Deposit Cash")

a = int(input("Please choose transactions: "))
if a==1:
    
    amt =int(input("Enter the  withdraw amount : "))
    if amt<100 or amt>10000:
        print("OUT OF LIMIT!!!!!!!!!!!")
    elif amt>bal :
         print("Insufficient Balance!!!")
    elif amt%100!=0:
        print("INVALID CASH")

    else:
         print("****************************************************************************")
         print("*                                                                          *")
         print("*                           Loading Transaction..                          *")
         print("*                                                                          *")
         print("****************************************************************************")
         print("****************************************************************************")
         print("*                                                                          *")
         print("*                           Please Collect Your Cash                       *")
         print("*                                                                          *")
         print("****************************************************************************")
         balance[y]=bal-amt
         print("Avilable Balance  : ",balance[y])

elif a==2:
     print("****************************************************************************")
     print("*                                                                          *")
     print("*                           Fetching Bank details..............            *")
     print("*                                                                          *")
     print("****************************************************************************")
     print("****************************************************************************")
     print("*                                                                          *")
     print("*                           Your Avilable Balance is :",bal                  )
     print("*                                                                          *")
     print("****************************************************************************")
elif a==3:
    if bal>2000:
         print("press '1' for 2000 Rupees")
         print("press '2' for 5000 Rupees")
         print("press '3' for 10000 Rupees")
         b=int(input("Please choose fast cash option :"))    
         if b==1:
             print("****************************************************************************")
             print("*                                                                          *")
             print("*                           Please Collect Your Cash                       *")
             print("*                                                                          *")
             print("****************************************************************************")
             balance[y]=bal-2000
             print("Avilable Balance  : ",balance[y])
         elif b==2:
             print("****************************************************************************")
             print("*                                                                          *")
             print("*                           Please Collect Your Cash                       *")
             print("*                                                                          *")
             print("****************************************************************************")
             balance[y]=bal-5000
             print("Avilable Balance  : ",balance[y])
         elif b==3 :    
             print("****************************************************************************")
             print("*                                                                          *")
             print("*                           Please Collect Your Cash                       *")
             print("*                                                                          *")
             print("****************************************************************************")
             balance[y]=bal-1000
             print("Avilable Balance  : ",balance[y])
         else:
             print("Invalid fast cash option")  
    else:
         print("****************************************************************************")
         print("*                                                                          *")
         print("*                          Insufficient balance to use fast cash..         *")
         print("*                                                                          *")
         print("****************************************************************************")
elif a==4:
     print("****************************************************************************")
     print("*                                                                          *")
     print("*                    DEPOSIT PER TRANSACTION LIMIT : 10000                 *")
     print("*                                                                          *")
     print("****************************************************************************")
     deposit=int(input("Amount to deposit :"))
     if deposit<=10000 and deposit%100==0:
         print("****************************************************************************")
         print("*                                                                          *")
         print("*                  Please Deposit the cash in the machine..                *")
         print("*                                                                          *")
         print("****************************************************************************")
         print("****************************************************************************")
         print("*                                                                          *")
         print("*             Sucessfully Deposited :",deposit                                )
         print("*                                                                          *")
         print("****************************************************************************")
         balance[y]=bal+deposit
         print("Avilable Balance  : ",balance[y])
     else:
         print("****************************************************************************")
         print("*                         SORRY!!!!!!                                      *")
         print("*                  Acceptable Denomination                                 *")
         print("*                  Rs.100, Rs.500, Rs200, Rs2000                           *")
         print("****************************************************************************")

        
       
        
else:
    print("Invalid transaction option") 
  
print("****************************************************************************")
print("*                                                                          *")
print("*                           THANKYOU FOR BANKING WITH US                   *")
print("*                                                                          *")
print("****************************************************************************")

