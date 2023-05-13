
n=10
if n%2==1:
    print("Weird")
else:
    if (n%2==0):
        if (n>=2 and n<5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")  
        else:
            print("Not Weird")

j=3
for i in range(3):
    print(i)

#LEAP YEAR
#Condition is it's divisible by 4 and not 100 or divisible by 400

def is_leap(year):
    leap = False
    if((year%4==0 and year%100!=0) or year%400==0):
        leap = True
    print("The year %d is: %s"%(year,leap))

#year = int(input())
is_leap(2000)

n=3
for i in range(n):
    print(i)

#Printing numbers as string in one line.
def print_oneline_str(n):
    s=""
    for i in range(1,n+1):
        s += str(i)
    print(s)  

print_oneline_str(5) #12345

#from array take the second highest one
# by using set to remove duplicates and them coverting to list to sort
def sort(arr):
    score = list(set(arr))
    print(sorted(score)[-2])

sort([1,3,4,4])



