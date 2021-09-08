# Dictionary METHODS (not from lpthw book)
# methods of working with dictionaries by examples

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "Michigan": "MI",
    "New York": "NY",
}
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville",
    "NY": "New York",
    "OR": "Portland",
}

states["Georgia"] = "GA"  # adds string to the dictionary

print(states)
# states.clear() - cleans dictionary

items = states.items()  # returns all pairs (key + value)
print(items)

dict_copy = states.copy()  # copies dictionary
print(dict_copy)

keys_of_dict = states.keys()  # returns all keys (left column)
print(keys_of_dict)

values_of_dict = states.values()  # returns all values (right column)
print(values_of_dict)

oregon1 = states["Oregon"]  # returns value by key
print(oregon1)

oregon2 = states.get("Oregon")  # looks for key and returns value
print(oregon2)

c = states.get("Texas")  # looks for key...
print(c)  # ...if key doesn't exist, result is None

d = states.get("NE", "Nevada")  # looks for pair (key + value)
print(d)  # ... if there isn't key, assigns the value specified in the search

keys = {"Arizona", "Alaska", "Colorado", "North California", "South California"}  # list
new_states_dict = dict.fromkeys(
    keys
)  # creates a dictionary with keys from 'keys' list and the default value of None
print(new_states_dict)

state_value = "Unknown abbreviation"
new_states_dict_2 = dict.fromkeys(
    keys, state_value
)  # creates a dictionary with keys from 'keys' list and values from state_value for all pairs
print(new_states_dict_2)

value = [1]
dic_a = dict.fromkeys(
    keys, value
)  # creates a dictionary with keys from 'keys' list and value [1] for all pairs
print(dic_a)

# if you change the value (this is the list), the contents of dictionary 'dic_a' will be changed
value.append(2)
print(value)
print(dic_a)

# to prevent it, we form the list based on 'value' veriable and use it for keys creating dictionary.
dic_b = {key: list(value) for key in keys}

# thus, if you change value variable, the contents of the dictionary isn't changed
value.append(3)
print(value)
print(dic_a)
print(dic_b)


print("\nThere is dictionary 'states': ", states)
print("I use the method .popitem() for this dictionary")
result = (
    states.popitem()
)  # removes the last key + value pair from the dictionary and returns it

print(f"After this method the {result} disappears from dictionary")
print("And now dictionary consists of: ", states)


print("\nThere is a dict 'states': ", states)
except_value = states.pop("Oregon")  # looks for value by key and deletes this pair
print("Delete: ", except_value)
print("There is a NEW dict 'states': ", states)

except_value_2 = states.pop(
    "Texas", "TE"
)  # Texas key isn't found, TE value is returned
print("Delete: ", except_value_2)
print("There is a NEW dict 'states': ", states)

# find_key = states.pop ('Texas') #Texas key isn't found, there is an error in this line
# print ('Delete:', find_key)

print("\nDictionary is ", states)
h = states.setdefault("California")
print("We create California key, but it already has value ", h)
g = states.setdefault("Texas")
print(
    "\nWe create Texas key, but its value is not specified, therefore, the value assigned by default is ",
    g,
)
print(states)
n = states.setdefault("Nevada", "NE")
print(f"\nWe create pair Nevada: NE, so Nevada key has value {n}")
print("\nNow the dictionary is: ", states)

print("\n")

states.update(
    North_California="NC", South_California="SC"
)  #'states' dictionary is updated adding two pair (key + value)
print(states)

states.update(cities)  #'cities' dictionary is added to 'states' dictionary
print("\nStates and cities are: ", states)
