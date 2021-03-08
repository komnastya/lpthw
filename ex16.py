from sys import argv 

script, filename = argv 

print (f"We are going to erase {filename}")
print ("If you don't want that, hit CTRL+C.")
print ("If you do want that, hit RETURN")

input ("?")

print ("Opening the file ... ")
target = open (filename, 'w')

print ('Truncating the file. Bye!')
target.truncate()

print ('Now I am going to ask you for three lines.')

line1 = input ('Line 1 is: ')
line2 = input ('Line 2 is: ')
line3 = input ('Line 3 is: ')

print ("I am going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()