#bank.py
#This programe will prompt the user and read in two money amounts (in cent), 
#add those two amounts together
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 


amount1 = input("Enter the first amount you would like to add (in cent) ")
amount2 = input("Enter the first amount you would like to add (in cent) ")

Total = (int(amount1) + int(amount2) ) / 100

print( 'Your Balance: ' + '€' +  str( Total ))





