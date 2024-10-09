import sys
import os # For some error checks 

def tokenize(file_name): # creating a tokenizer from scratch
    token_frequency = {} # A dictionary to record the frequency of each token
    current_token = [] # This list will be used to store the alphanum characters

    try:
        with open(file_name, 'r', encoding = 'utf-8') as file: # Opening the file in read mode Using utf-8 encoding
                while True:
                    char = file.read(1) # This reads the file character by character
                    if not char: # Checks the end of the file 
                        if current_token: # Checks that the list is not empty
                            token = "".join(current_token).lower() # This lines joins the string & normalize the string
                            token_frequency[token] = token_frequency.get(token, 0) + 1# In order to use the get() for dictionary I used https://docs.python.org/3/library/stdtypes.html#dict.get
                            current_token = [] 
                            break
                    if char.isalnum(): # Checks if the character is a letter or a number
                        current_token.append(char) # If true, then append it to the token list 
                    else:
                        if current_token:
                          token = "".join(current_token).lower() # This lines joins the string & normalize the string
                          token_frequency[token] = token_frequency.get(token, 0) + 1 # In order to use the get() for dictionary I used https://docs.python.org/3/library/stdtypes.html#dict.get
                          current_token = []

    except FileNotFoundError: # I used this site https://docs.python.org/3/library/exceptions.html
        print("File doesn't exist")


    return token_frequency

def computeWordFrequencies(tokens):
    token_frequency = {} # A dictionry to store token count
    for token in tokens: # Iterate over the list of tokens
        if token in token_frequency: # Checks if the token is in the token dic
            token_frequency[token] += 1 # Increment if a token is found in the dic
        else:
            token_frequency[token] = 1 # Initialize the token with a count of 1
    return token_frequency

    

def main():
    if len(sys.argv) < 2: #Checks the number of command line arguments
        print("The command line argument should be: python Text_Processing.py <filename>" )
        return 
    
    file_name = sys.argv[1] # This is assigns the variable file_name to the
                            # first command line arguement 
    

    
