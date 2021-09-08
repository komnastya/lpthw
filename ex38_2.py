# ex38

ten_things = "Apple Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(" ")
print("Now array consists of ", " ".join(stuff))

print(f"Array has {len(stuff)} items\n")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

for ignore in stuff:
    next_one = more_stuff.pop()
    stuff.append(next_one)
    if len(stuff) == 11:
        break
    print("element ", next_one, " is added to the array")
    print(f"Now the array has {len(stuff)} items")
    print(stuff, "\n")
