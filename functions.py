def multiply_numbers(a, b):

    return a * b
# Call the multiply_numbers function and print the result
num3 = 4
num4 = 2
result = multiply_numbers(num3, num4)
print(f"The product of {num3} and {num4} is: {result}")

#Lambda function
square = lambda x:x**2
print(square(5))

multiply = lambda a,b:a*b
print(multiply(3,4))

x=lambda m,n,o:m+n+o
print(x(2,3,4))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

'''
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.
'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 

#default value
def add(a,b=10):
   return a+b

print(add(9))    #prints 19
print(add(9,5))  #prints 14 as the value is provided

#Passing list as argument
def food(food):
   for x in food:
      print(x)

fruits=["banana","apple","mango"]
food(fruits)