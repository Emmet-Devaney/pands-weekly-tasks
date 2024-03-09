#this function serves to calculate the approximate square root of a positive number

def square_root():
    number = input("Please enter a positive number: ")

    number = float(number)
    
    if number <= 0:
        print("That is not a positive number.")
        return
    
    epsilon = 0.0000001  # Epsilon is an arbitrary positive number. This value can be adjusted for accuracy.
    guess = number / 2   # Starting point for calculation

    while abs(guess * guess - number) > epsilon: # looping to get the root
        guess = (guess + number / guess) / 2

    print(f"The square root of {number} is {guess}")

# Call the function to calculate and print the square root
square_root()