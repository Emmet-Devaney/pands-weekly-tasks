#The purpose of this program is to identify if it is the weekend or weekday
#The program imports the module "datetime" to identify the curent date, then uses a list to identify what day of the week it is
#the list is identified from [0, ..., 6], being [Monday, ..., Sunday]
#a different output is decided using an if else statement

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Extract the weekday 
weekday_number = current_datetime.weekday()

# Define a list to map weekday numbers to day names
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the current day
print("Current Day:", days_of_week[weekday_number])

# Check if it's a weekend or weekday
if weekday_number < 5:  # Monday to Friday (0 to 4)
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")




