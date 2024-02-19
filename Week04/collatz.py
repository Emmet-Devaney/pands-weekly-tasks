#A positive interger will be inputed
#if the input is even, the number wil be divided by 2
#if the number is odd it will be multiplied by 3 and 1 will be added
#the sequence will end once the sequence reaches 1

starting_number = input('Please enter a postive interger: ')

starting_number = int(starting_number)  

sequence = [starting_number]

while starting_number != 1:
        if starting_number % 2 == 0:
            starting_number = starting_number // 2
        else:
            starting_number = 3 * starting_number + 1

        sequence.append(starting_number)

print(f"Collatz sequence for {starting_number}: {sequence}")