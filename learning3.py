#09/05/2023
'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

 -> List is a collection which is ordered and changeable. Allows duplicate members.
 -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 -> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 -> Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#TUPLES () (ORDERED, UNCHANGEABLE, ALLOW DUPLICATES)

#Modifications in Tuple by converting it to list and then we have to do

t = (1,'apple',True, 1)
print(t)
print(type(t))
print(len(t))

t1=("apple",) #Tuple
t2=("apple") #Not a tuple it is a string
print(type(t1))
print(type(t2))
print(t1, "\n", t2)

#Tuple accessing is same as LIST
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[-1])
print(thistuple[::-1])
print(thistuple[1::2]) #even index values
print(thistuple[::2]) # odd index values

if "cherry" in thistuple:
    print("Hooray! you won")


#UPDATE TUPLES BY CONVERTING IT TO LIST
l=list(thistuple)
print(l)
l[1]="green apple"
thistuple=tuple(l)
print(thistuple)
print(len(thistuple)) 

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print(len(thistuple))


fruits=("apple", "kiwi", "melon", "mango")
fruits=list(fruits)
fruits.remove("kiwi")
print(fruits)
del fruits
#print(fruits)

#Looping through tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

#index loop through in tuple
for i in range(len(thistuple)):
   print(i) #displays index

#while loop
tup = ("apple", "banana", "cherry")
i = 0
while i < len(tup):
  print(tup[i])
  i = i + 1 

#joining of tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuple values in tuple
fruits = ("apple", "banana", "cherry")
fruits = fruits * 2
print(fruits) 

#counts no.of times the value occurs
a=fruits.count("apple")
print(a)

#shows the index of occurance normally the first one
b=fruits.index("banana")
print(b)


'''
METHODS IN TUPLE
count()
index()
'''