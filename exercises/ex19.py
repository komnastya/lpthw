#ex19

def cheese_and_crackers (cheese_count, crackers_count):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {crackers_count} boxes of crackers!")
    print ("That's enought for party")
    print ("Get a blanket.\n\n")

print ('We can just give thee function numbers directly')
cheese_and_crackers (20, 30)

print ("Or we can use fariables from our script")
a = 50
b = 60 
cheese_and_crackers (a,b)

print ('We can even do math inside too:')
cheese_and_crackers (17+13, 9+2)

print ("And we can combine the two, variables and math")
cheese_and_crackers (a+10, b + 35)
