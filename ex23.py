#ex23

import sys
script, input_encoding, error = sys.argv

def main (language_file, encoding, errors): #main function; 'encoding' - by what rules, errors - what to do in case of an error
    line = language_file.readline() #read file line by line

    if line: #checks if there is something in the string
        print_line(line, encoding, errors) #if the string is not empty, prints the string and ...
        return main (language_file, encoding, errors) #... runs the same function again


def print_line (line, encoding, errors): #function encodes the string read on line 6
    next_lang = line.strip() #removes spaces at the end and at the beginning of a line, but not inside the line itself
    raw_bytes = next_lang.encode (encoding, errors = errors) #string is converted in bytes
    cooked_string = raw_bytes.decode(encoding, errors = errors) #bytes are converted in string

    print (raw_bytes, '<===>', cooked_string) #display the result on the screen, on the left are bytes in utf-8 encoding, on the right is text


languages = open ('language.txt', encoding = 'utf-8') #read file, decode first time

main (languages, input_encoding, error) #call function
