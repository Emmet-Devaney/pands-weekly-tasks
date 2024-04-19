#Open the file specified in the command line argument and read its contents
#Count the occurrences of the letter 'e' in the text provided
#Check for potential errors such as missing command-line arguments, non-existent files, or files that are not text files.
#Print the count of 'e's

import sys

def count_es(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            e_count = text.count('e')
            return e_count
    except FileNotFoundError:
        print("File not found.")
        return None
    except IOError:
        print("Error reading the file.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python es.py <filename>")
    else:
        filename = sys.argv[1]
        if not filename.endswith('.txt'):
            print("Please provide a text file.")
        else:
            e_count = count_es(filename)
            if e_count is not None:
                print(e_count)