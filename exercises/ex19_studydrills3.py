# ex19

print("What is your name?", end=" ")
name = input()

print("How old are your?", end=" ")
age = input()


def myfriends(name, age):
    print(f"Hello, {name}! You are my friend")
    print(f"You are {age} years old. Right?")
    print(f"{name}, how many countries have you visited in 2020? ", end=" ")
    number = input()
    print(f"{name}, what countries have you visited in 2020? ", end=" ")
    chname = input()
    print(
        f"{name} is {age} years old and she has visited {number} countries in 2020. There are {chname}"
    )


myfriends(name, age)
myfriends(
    "Julia", "27"
)  # the name and age are in the script, function asks only for information about visited countries

name1 = "Kate"
age1 = "26"
myfriends(name1, age1)
