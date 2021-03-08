from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying from {from_file} to {to_file}")

in_file = open (from_file) #open file
indata = in_file.read() #read file

print (f'The input file is {len(indata)} bytes long')

print (f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open (to_file, "w") #open the 2nd file in read and write mode
out_file.write(indata) #write information from the first to the second file

print("Alright, all done.")
out_file.close()
in_file.close()
