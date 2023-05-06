#Python Variables, Strings, Integer, Float

age = "45"
sal = "145.83"
name="John"
height=5.6


print("My name is "+name+" and my age is "+age+" and my salary is CAD " +sal) #concatenate only strings
print("My height is:",height)
print("My height is:",int(height))
print(type(age))
print(type(height))

a,b,c='a','b','c'
print(a,b,c)

a=int(100.10)
b=float(66.5)
print(a,b)
print(type(a))
print(type(b))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a>b)
print(a<b)
print(a!=b)
print(a==b)


x=bool(True)
print(x)
print(type(x))

m=int(21e3)
m1=20e3
m2=1e-3
n=20+3j
print(m,'\n',n)
print(type(m),'\n',type(n))
print(m1,'\n',n)
print(type(m1),'\n',type(m2))

v="Im good at coding, bcoz I practice it everyday"
print(v)

#Triple quotes to write multiline output
y='''Im good at coding,
bcoz I practice it everyday'''
print(y)

'''multiline 
comment'''


g='I\'m Good'
h='yes i know' 
print(g+h)
print(len(g))
print(g[2:5]) #m,g
print(g.upper())
print(g.lower())
print(g.split()) # list as output
j=g.split()
print(type(j))

c=list(('apple','mango','grapes'))
print(c)
print(type(c))

d=tuple(('apple','mango','grapes'))
print(d)
print(type(d))

e=set(('apple','mango','grapes'))
print(e)
print(type(e))

f=dict({'a':100,'b':50,'c':25})
print(f)
print(type(f))



