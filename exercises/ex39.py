#ex39

states = { #creates dictionary
    'Oregon': 'OR',
    'Florida' : 'FL',
    'California': 'CA'
}

states ['New York'] = 'NY' #adds elements to 'states' dictionary
states ['Michigan'] = 'MI'


cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}


cities ['NY'] = 'New York' #adds elements to 'cities' dictionary
cities ['OR'] = 'Portland'


print ('-' * 10)
print ("NY State has: ", cities['NY']) #displays value by key
print ("OR State has: ", cities['OR'])


print ('-' * 10)
print ("Michigan's abbreviation is: ", states ['Michigan'])
print ("Florida's abbreviation is: ", states ['Florida'])


print ('-' * 10)
print ("Michigan has: ", cities [states ['Michigan']])
print ("Florida has ", cities[states ['Florida']])


print ('-' * 10)

for state, abbrev in list(states.items()):
    print (f"{state} is abbreviated {abbrev}")


print ('-' * 10)
for abbrev, city in list(cities.items()):
    print (f"{abbrev} has the city {city} ")


print ('-' * 10)
for state, abbrev in list(states.items()):
    print (f"{state} is abbreviated {abbrev}")
    print (f"and has city {cities[abbrev]}")

print ('-' * 10)
state = states.get ('Texas')

if not state:
    print ('Sorry, no Texas')

city = cities.get ('TX', 'Does Not Exist')
print (f"There city for the state 'TX' is: {city}")
