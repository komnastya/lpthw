#ex35
from sys import exit
#sys interacts with the OS, imports functions from the OS



def gold_room ():
    print("This room is full of gold. How much do you take?")

    choice = input ("> ")
    if "0" in choice or "1" in choice: #if 0 or 1 is in user response
        how_much = int(choice) #converting into number format

    else:
        dead ("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit (0) #immediate program abort
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False #the variable is assigned a False value

    while True: #loop always runs, exits/stop with dead function
        choice = input ("> ")

        if choice == "take honey":
           dead("The bear looks at you then slaps your face off.") #program abort through the dead function
        elif choice == "taunt bear" and not bear_moved: #not bear_moved  = True
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True # after the loop is executed, and "taunt bear" is selected, bear_moved on line 26 becomes False - the while loop has changed it!
            #so the next time the 1st elif is NOT executed when taunt bear is selected, because True and not True on line 33 is False
            #Those the second time, the first elif is already False, thus the program proceeds to the next condition elif choice == "taunt bear" and bear_moved:
            ## which with the changed bear-moved value is already True, here True and True -> True
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved: #this condition is not met while bear_moved = False.
        #as soon as the cycle changes the value of bear_moved to True, the open door will work, because True and True -> True
            gold_room ()
        else:
            print ("I got no idea what that means")


def cthulhu_room ():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input ("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead ("Well that was tasty!")
    else:
        cthulhu_room ()

def dead (why):
    print (why, "Good job")
    exit (0) #immediate program abort

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room ()
    elif choice == "right":
        cthulhu_room()
    else:
        dead ("You stumble around the room untill you starve.")

start()
