#12/05/2022

'''
LOOPS IN PYTHON
It supports logical conditions of mathemtical operators
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
'''
import time
import re

#If elif else loop

#only one condition works
a=100
b=10
c=1
if a>b:
    print("A > B")
elif a==b:
    print("A == B")
else:
    print("A < B")

#One line if
if a>b: print("A > B")  #if a value changes <=B then this print wont work

#Short hand if else
print("Manoj") if a > b else print("Pavan")
print("RCB") if a!=b else print("RBC")

#Multiple else statements
a=100
b=10
print("A") if a > b else print("A=B") if a == b else print("B")

#and or & not
if a>b and b>c:
    print("A>B>C")
elif a>b or b<c:
    print("A>C<B")

print("A<B") if not a>b else print("A>B")

start=time.time()
a=0.1
b=0.010
c=1
print("A") if a>b>c else print("B") if a<b>c else print("C")
end=time.time()
print("Time Execution1: ",{end-start})
#A a=100, b=10, c=1
#B a=5, b=10, c=1
#C a=0.1 b=0.2 c=1

#Nested IF
#pass statement to avoid error
m=10
n=10
if(m==n):
    m=0
    n=10
    if(m>n):
        pass
    else:
        print("MANOJ")


#WHILE LOOPS
print("WHILE LOOPS")
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

#break statement to stop and come out of the loop

i = 0
while i<5:
    print(i)
    i+=1
    if (i==4):
        break
print("Break executed")

#continue : stop current iteration and continue with rest

i = 1
while i<5:
    print(i)
    i+=1
    if (i==3):
        print("Continue executed")
        continue

j = 0
while j < 6:
  print(j)
  j += 1
else:
  print("j is no longer less than 6")


#FOR LOOPS
print("FOR Loops")
for x in range(1,3):
    print(x)

for y in range(1,10,4):
    print(y)

for x in range(3):
  print(x)

fruits=["apple","banana","mango"]
for x in fruits:
    print(x)

count=0
for x in "banana":
    count+=1
    if(x=='n'):
        print("The index of n: ",count)

for x in fruits:
    if 'a' in x:
        print("A is present in: ",x)

for x in fruits:
    count=0
    for y in x:
        if(y=='a'):
            print("A is present at index: ",count,"of fruit: ",x)
        #else:
            #print("Letter not present")
        count+=1

#using Regular expression
fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    match = re.search(r'a', fruit) #gives at only first occurance
    if match:
        print(f"A is present at index: {match.start()} of fruit: {fruit}")
    #else:
        #print("Letter not present")


for x in fruits:
    matches = re.finditer("a", x)   # at all occurences
    for match in matches:
        print(f"The letter 'a' was found at index {match.start()} in the letters of {x}")
