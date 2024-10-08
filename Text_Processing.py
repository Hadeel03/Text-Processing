import sys
import os # For some error checks 

def tokenize(file_name): # creating a tokenizer from scratch
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file: # Opening the file in read mode
                 #Token logic goes here                                     # Using utf-8 encoding
            pass
    except FileNotFoundError: # I used this site https://docs.python.org/3/library/exceptions.html
        print("File doesn't exist")

    return

def main():
    if len(sys.argv) < 2: #Checks the number of command line arguments
        print("The command line argument should be: python Text_Processing.py <filename>" )
        return 
    
    file_name = sys.argv[1] # This is assigns the variable file_name to the
                            # first command line arguement 
    
