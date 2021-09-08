# ex15

from sys import argv

script, filename = argv

txt = open(filename)  # the txt variable is assigned data from an open file

print(f"Here's your file {filename}")
print(txt.read())  # show (=read) file

print("Type the filename again:")

file_again = input("> ")  # get file name
txt_again = open(file_again)  # "open" file
print(txt_again.read())  # "read" = show
