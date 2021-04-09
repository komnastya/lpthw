#ex20

from sys import argv

script, input_file = argv

def print_all (f):
    print (f.read()) #the file is read and the CURSOR is at the END of the file

current_file = open(input_file) #open / unpack the file - extract the text

print ("\nFirst, let's print the whole file: \n")
print_all (current_file) #display text on the screen


def rewind(f):
    f.seek(0)  #return the CURSOR to the BEGINNING of the file

def print_a_line (linecount, f):
    print (linecount, f.readline()) #reads text line by line

print ("\nNow let's rewind, kind of like a tape.\n")

rewind (current_file)
print ("Let's print three lines:")

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)
