#08/05/2023
'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

 -> List is a collection which is ordered and changeable. Allows duplicate members.
 -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 -> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 -> Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#LISTS (Ordered, Changable and allow duplicates)
#List items are indexed
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

print(mylist[:2])
print(mylist[1:3])

#iterating
for x in mylist:
    print(x)


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)


#Small program of lists
numbers = []
strings = []
names = ["John", "Eric", "Jessica",1,2,3,4]
print("Length of names list: %d" % len(names))

# write your code here
second_name = names[1]


for x in names:
    a=type(x)
    if a == str:
        strings.append(x)
    else:
        numbers.append(x)

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#Access List Items
#Through Indices
# list[2:3]
# list[::-1] to make reverse of a string
# [:] all elements [:3] first 3 elements [2:] from 3rd element

#in operator
names=['John','Rick']
name = "Joe"
if name in names:
    print("Your name is either John or Rick.")
elif(name == names[0]):
    print('Your name is %s' % name)
else:
    print('Your name is %s' % name)

fruits = []
fruits.append('apple')
fruits.append('banana')
fruits.append('cherry')
fruits.append('kiwi')

new_a_fruits=[]

for x in fruits:
    if 'a' in x:
        new_a_fruits.append(x)
    
print('Fruits with letter a in them:', new_a_fruits)

#Change the list items
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) 

#Insert list item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add a list item by append, insert and extend
fruits1=['mango']
fruits2=tuple(('strawberry','raspberry'))
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.insert(2,'kiwi')
thislist.extend(fruits1)   #extends with a given list
thislist.extend(fruits2)   #extends tuple
print(thislist) 


#Remove an item from list by remove (item specified), del (deletes specified index  /  no arguments whole list), pop (last index of item) 
#Clear() clears elements in the list and it will be an empty list.
fruits = ["apple",'kiwi','orange','berry', "banana", "dragon fruit", 'cherry']
myfruits=[]
mynewfruits=[]
fruits.sort() #sorting of list in ascending
print("Sorted fruits:",fruits)
fruits.sort(reverse = True) #sorting of list in descending
print("Reverse Sorted fruits",fruits)
a=fruits.index('cherry')
print("Index of cherry:",a)
myfruits=fruits.copy()
print('Copy of fruits to new list:',myfruits)
mynewfruits=list(fruits)
print('Copy of fruits:',mynewfruits)
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
del fruits[1]
print(fruits)
fruits.clear()
print(fruits)
del fruits
#print(fruits) no fruits list will be there

#JOIN Lists (by + operator, append and extend)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


#LOOP through lists
a = ["apple", "banana", "cherry"]
e=[]
for x in a:
  print(x) 
  if 'a' in x:
      e.append(x)
print('New List:',e)

b = ["apple", "banana", "cherry"]
for i in range(len(b)):
  print(b[i]) 

c=["apple", "banana", "cherry"]
d=[]
for i in range(len(c)):
    if 'c' in c[i]:
        d.append(c[i])
print("New List:",d)

#While
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

'''
Methods in List
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
'''
