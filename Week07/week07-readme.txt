# E Counter

## Description
This Python script counts the amount of the letter 'e' in a text file.

## Usage
1. Run the script using Python, and provide a text file.
2. The script will count the amount of the letter 'e' in a text file supplied and print the result.

## Details
- The script defines a function `count_es(filename)` to count the amount of the letter 'e' in a text file.
- It reads the contents of the file and uses the `count()` method to count the occurrences of 'e'.
- If the file is not found or cannot be read, an appropriate error message is displayed.
- If the filename provided does not end with '.txt', the script will notify the user.
- The main block of the script checks for the correct number of command-line arguments, validates the filename, calls the `count_es()` function, and prints the result.

## Notes
- This script allows users to count the occurrences of 'e' in any text file by providing the filename as a command-line argument.