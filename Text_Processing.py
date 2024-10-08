import sys

def main():
    if len(sys.argv) < 2: #Checks the number of command line arguments
        print("The command line argument should be: python Text_Processing.py <filename>" )
        return 
    
    file_name = sys.argv[1] # This is assigns the variable file_name to the
                            # first command line arguement 