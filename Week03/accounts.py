#When a bank account number of 10 charachters is entered
#the program will display the last 4 digits
#while the previous 6 will display X's
#if a charachter length greater than 10 is entered the program will only factor the first 10 digits inputed, and display the last 4 digits

account_number = input('please enter your 10 digit account number: ')

displayed_account_number = (account_number[6:10])

print('Your Account Number: XXXXXX' + displayed_account_number)
