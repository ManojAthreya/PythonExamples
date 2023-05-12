#11/05/2023
'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

 -> List is a collection which is ordered and changeable. Allows duplicate members.
 -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 -> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 -> Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#Dictionaries {'key':'value'} (Ordered, changable, No duplicate values)

#duplicate values are ignored and if value is different recent value is taken for that key.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(car)
print(car['brand'])
print("Dictionary length:",len(car))
print(type(car))

#Accessing dictionary items

#1
print(car['colors'])
print(car['brand'])
print(car['year'])

#2 using get()
print(car.get("model"))
print(car.get("year"))
print(car.get("brand"))
print(car.get("color")) #None is displayed if key is wrong

print(car.keys())  # returns keys in the dictionary
print(car.values()) # returns values in the dictionary
print(car.items()) #gives key value pairs of the dictionary

if "colors" in car:
    print("Colors option available in car")


#Changing / adding values in dictionary

#1
car["brand"]="BMW"
print(car)

#new key value pair added
car["sold"]=225
print(car)

#2 using update
car.update({"model":"X3"})
print(car)

#new key value pair added
car.update({"sold":500})
print(car)

#Removing items from dictionary pop(), del(), clear()

print("Original dictionary:",car)
car.pop('colors') #removes specified key value pair
print(car)
car.popitem()   #removes sold as it was last inserted
print(car)

#del car['model'] # removes the specified as well as the whole dictionary.
#car.clear() #empties the dictionary

#Looping in Dictionaries

for x in car:        #prints keys of the dictionary
    print(x)

for x in car:        #prints values 
    print(car[x])

for x in car.keys():
    print(x)

for x in car.values():
    print(x)

#Loop through keys and values
for x,y in car.items():
    print(x,y)


cars1=car.copy()
print(cars1)
cars1['type']="disel"
cars1['colors']=["red","yellow"]
print(cars1)
print(cars1.get("colors"))


#Nested Dictionaries

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(myfamily["child2"]["name"]) 
print(myfamily)   #displays whole dictionary
print(myfamily.keys())
print(myfamily.values())
print(myfamily.items())
print(myfamily.get('child1'))
print(myfamily.popitem())
print(myfamily)

for x in myfamily:
    print(x)

for x,y in myfamily.items():
    print(x,y)


'''
Dictionary Methods

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''
