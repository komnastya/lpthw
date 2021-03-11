#ex38

ten_things = "Apple Oranges Crows Telephone Light Sugar" #string
print (ten_things)
print ("Wait there are not 1- things in that list. Let's fix that.")

stuff = ten_things.split(' ') #string is split into words and the array stuff is formed
print (stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] #create array more_stuff

while len(stuff) != 10: #a loop is started and will be executed if the array stuff has less than 10 items
    next_one = more_stuff.pop() #the last element of the more_stuff array is assigned to the variable
    print ("Adding: ", next_one)
    stuff.append(next_one) #the last element of the more_stuff array is added to the stuff array
    print (f"There are {len(stuff)} items now") #print the length of the stuff array

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print ('The second element is ', stuff[1]) #display the second element of the array (the first one has index 0)
print ('The last element is', stuff[-1]) #display the last element of the array
#there is an array element by index in brackets, which can be assigned to a variable and / or displayed

print (stuff.pop()) #remove and return the last element of the array

print (' '.join(stuff)) #displays array elements without [], separated by a quoted character (in this case, a space ' ')
print ('&'.join(stuff[3:6])) #displays the elements 4,5,6 (indices 3,4,5) of an array without [] separated by the character specified in quotes (in this case, &)
