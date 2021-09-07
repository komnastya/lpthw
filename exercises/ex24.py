# ex24

print("Let's practice everything.")
print("You'd need to know 'bout escape with \\ that do: ")
print("\n newlines and \t tabs.")

poem = """
\t THe lovely world
with logic so firmly planted
cannot discern \n the needs of love
no comprehend passion from intuition
and requiers an explonation
\n\t\twhere there is none.
"""

print("----------------------")
print(poem)
print("----------------------")  # display text on the screen

five = 10 - 2 + 3 - 6
print(f"This is should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return (
        jelly_beans,
        jars,
        crates,
    )  # create a function that performs calculations and assign the result to three variables


start_point = 10000
beans, jars, crates = secret_formula(
    start_point
)  # three variables get the result of the function


print(
    "With a start point of: {}".format(start_point)
)  # insert the variable into the printed line using .format

print(
    f"We'd have {beans} beans, {jars} jars, and {crates} crates"
)  # insert the values ​​of the variables from line 31, which are calculated by secret_formula

start_point = start_point / 10  # change input data

print("We can also do this that way:")

formula = secret_formula(
    start_point
)  # the function is started with new input data and the result (3 variables) is assigned to one variable formula

print(
    "We have {} beans, {} jars, and {} crates.".format(*formula)
)  # using .format(* ) insert data in the string
# three function values ​​that have been assigned to one formula variable
