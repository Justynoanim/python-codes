SeatTaken=[2,34, 40, 32, 7,50]
print("Available seat:")
for n in range(1,51):
    if n in SeatTaken:
        continue
    print(n)

Mujidastaff= ['loveth', 'nike', 'faith','tolu']
for s in Mujidastaff[:2]:
    print(s)
    print(len(s))

def python():
    print("Justice work in mujida pharmacy")
    print("justice is a pharmacist")
python()


x=5
for x in range(0,5):
    print(x)
x="Justice"
print(type(x))
x=2.56
print(type(x))
x=2
print(type(x))
Myname_is="Justice"
print(Myname_is)
a,b,c="Nike", "Loveth", "Tolu"
print(a)
print(b)
print(c)

Loveth=Nike=Tolu=Faith=Mujidastaff
a,b,c,d=Mujidastaff
print(a)
print(b)
print(c)
print(d)
a=b=c= "orange"
print(a)
print(b)
print(c)

m="python to the world"
print(m)

m="I "
n="Love "
o="you "
print(m+n+o)
print(m,n, o)

x=5
y=2
z=(x+y)
a="John"
print(z,a)

x=29/3
y=int(x)
print(y)

x=int(3)
print(type(x))
y=int(3.21)
print(type(y))
z=int(int('3'))
print(z)
print(type(z))

a='Hello'
print(a)

a="A noun is a name of any person, animal, place or thing"
print(a)
print(a[0])
print(a[2])
print(a[:2])
print(a[2:])
print(a[1])
print(len(a))

from urllib import request


a='Mr Aloba is the director at Jit solutions'
print(a[:2])
print(a[-2])
print(a[3])
#for i in a:
    #print(i)
print(len(a))
print(a[4:])
print(a[-8:])
print(a[:-8])
print(a[:41])
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("Aloba", "Justice"))
b=a.strip(",")
print(b)
c="Good"
d="  Morning \n Good Afternoon"
print(c + d)

#string formating
a=  35
b="  Justice"
#print(a+b)
print("My name is {b} , and I am {a}. yrs old".format(a=35, b="Justice"))
print(f" My name is {b}  and I am {a} yrs old")
#print("My name is {b} and I am {a} years old today".format (b,a))

h="Valentine"
print(h)
print(type(h))
print(h[1])
print(len(h))
for i in h:
    print(i)
print("Va" in h)
Anim=("Mary", "Reginald", "Valentine")
print(Anim)
print("Valentine" in Anim)
print("Mary" in Anim)
print("Reginald" in Anim)
print(len(Anim))
for i in Anim:
    print(i)

Anim=("Mary", "Reginald", "Valentine")
i=0
while i < len(Anim):
    print(Anim[i])
    i+=1


#if 'Aloba' in a:
#print('yes, 'Aloba' is there')
print(10>2)
print(5==5)
a=200
b=5
if a>b:
    print(" a is greater than b")
else:
    print(" b is less than a")
print("Hell word")
#print("Justice")


number=[5,15,6,2,91,90,101,23,50]
a=[]
for item in number:
    if item%5==0:
        a.append(item)
print(a)

for item in number:
    if item%5==0:
        a.append(item)
#print(a)

a=[]
print(a)
x=["Loveth", "Nike", "Tolu", "Blessing", "Faith", "Naomo", "Seun"]
print(x)
x.remove("Tolu")
print(x)
x.pop(0)
print(x)
del x
#print(x)
x.clear()
print(x)

s=["Loveth", "Nike", "Tolu", "Blessing", "Faith", "Naomo", "Seun"]
s.Sort()
print(s)

list1=[1,2,3,4,5]
list2=list1.copy()
print(list2)

a=[1,2,3,4,5]
x=["Loveth", "Nike", "Tolu", "Blessing", "Faith", "Naomo", "Seun"]
c=a+x
print(c)



list=[1,2,3,4,5]
list[2]


