#10/05/2023
'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

 -> List is a collection which is ordered and changeable. Allows duplicate members.
 -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 -> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 -> Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#SET {} (UNORDERED, UNCHANGABLE, UNINDEXED)

#Once set is created you cannot change the items but you can add or remove items.

a = {"apple", "banana", "cherry",1,2}
print(a)                               #for each output the index of strings are shuffled.
print(type(a))
print(len(a))

#loop through sets
for x in a:
    print(x)

print("cherry" in a) #Boolean value

#To add new items to a set one value at a time
a.add("kiwi")
a.add("mango")
a.add("apple")
print(a)

#no duplicates it executes but not add that item to the set.

#UPDATE method adds not only set but list and tuples and the end goal is set.
thisset = {"apple", "banana", "cherry"}
s2={"a","b","c"}
mylist = ["kiwi", "orange"]
mylist1 = ["d"]
mytuple=("mango",)
thisset.update(mylist,mytuple)  # accepts multiple arguments
thisset.update(mytuple)
s3=thisset.union(s2)
s4=thisset.union(mylist1)
print(thisset)
print(type(thisset))
print(len(thisset))
print(s3)
print(s4)

#Remove set items has remove(), discard(), pop(), clear(), del

s = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
s.remove("mango") #delete mango if that element not there raises error
print(s)
s.discard("kiwi") #deletes kiwi if that element not present does not raises the error
print(s)
s.pop()   #randomly deletes an element
print(s)
s1=s          #copy of set
print(s1)
print(type(s1))
print(s)
s.clear() #cleares the set elements
print(s)
del s    #deletes the entire set

#Methods in Set
'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''