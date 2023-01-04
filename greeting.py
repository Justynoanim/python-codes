import Module #import Module as md
Module.greeting("Ayokunle")
V=Module.cars
print(V)
V=Module.cars.items()
for x,y in V:
    if x =="Car":
        break
    else: print(x,y)



import platform
x=platform.system()
print(x)
v=platform.processor()
print(v)
p=dir(platform)
print(p)

from Module import greeting
print(greeting("Joshua"))

#Date time module

import datetime
x=dir(datetime) # To check function of a modue
print(x)
y=datetime.MAXYEAR
print(y)
z=datetime.__file__
print(z)
s=datetime.MINYEAR
print(s)

x=datetime.datetime.now()
print(x)
print(x.year) # to check year
print(x.strftime("%A")) # to check day
x=datetime.datetime(2022,9,8)
print(x)
print(x.strftime("%B"))



#Python Maths
a=min(5,10,2)
print(a)
b=max(5,10,2)
print(b)

c=abs(-7.39)
print(c)

d=pow(5,2) # 5 or 5**2
print(d)

import math
c=dir(math)
print(c)

e=math.sqrt(25)
print(e)
f=math.ceil(3.5)
g=math.floor(3.5)
print(f)
print(g)
print(math.pi)

z=math.sin(25)
print(z)
a=(f"{z:.2f}")
print(a)

s =abs(float(a))
print(s)

a="Ayokunle"
b=1
print(a +b)

#json
import json


#Assignment
#Q1
s=datetime.datetime.now()
print(s.strftime("%a"))

#Q2
s=datetime.datetime.now()
print(s.strftime("%d"))

#Q3
s=datetime.datetime.now()
print(s.strftime("%Y"))

#Q4

#Q6
s=datetime.datetime.now()
print(s.strftime("%X"))

#Q7
s=datetime.datetime.now()
print(s.strftime("%%"))