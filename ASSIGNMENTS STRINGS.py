#1
# X="what is your name"
# a=input("what is your name>")
# print(a)
# print(a[::2])

#2
A=[5,2,10,100,25,62,43,70]
for A in A:
    if A%5==0:
        print(A)


 #3
    m="florida"
    print(m[2:5])

    N="GoodDay"
    print(N[2:5])
#6

    A = "Adewumi"
    print("wu" in A)

#7
    A = ["Justice", "is", "A", "Student", "of", "jit", "solutions"]
    for A in A:
      print(A)

a="PHYTHON IS GREAT"
print(a.casefold())


#python set
#difference()
#intersection_update()
#pop()
#union()

#difference #it is used to return diff bw the 2 sets. it return a set that contain item(s) that only exist
a={"apple", "Banana", "Cherry"}
b={"Oranage", "Mango","apple"}
c=a.difference(b)
print(c)

A={10,20,30,40,80} # A={10,20}
B={100,30,80,40,60} #B={100,60}
C=B.difference(A)
print(C)


x={"a", "b", "c"}
y={"c", "d", "e"}
z={"f", "g", "c"}
x.intersection_update(y,z)
print(x) #Return items present in the 3 sets

A={1,2,3,4}
B={2,3,4,5,6}
C={4,5,6,9,10}
A.intersection_update(B,C)
print(A)


#pop() #It removes randam item from the set
Cars={"Toyota", "Benz", "Honda", "Ford"}
#Cars.pop()
#print(Cars)
x=Cars.pop() #it returns the removed item
print(x)
print(Cars)

#Union() #It returns a set that contains items from both sets but excluding the duplicate.
a={"apple", "Banana", "Cherry"}
b={"Oranage", "Mango","apple"}
c=a.union(b)
print(c)

A={1,2,3,4}
B={2,3,4,5,6}
C={4,5,6,9,10}
D=A.union(B,C)
print(D)


# import math
# def inputtt():
#     a=int(input("value of a >"))
#     b=int(input("value of b >"))
#     c=int(input("value of c >"))
#     return a,b,c
# def solve(a,b,c):
#     e=-b
#     f=(e**2)
#     g=4*a*c
#     h=math.sqrt(f-g)
#     i= e+h
#     k = float(i/(2*a))
#     l =e - h
#     z=float(l/(2*a))
#     return  k,z
# def output(k,z):
#     print(f"{k:.2f} or {z:.2f}")
# d = inputtt()
# P = solve(d[0],d[1],d[2])
# output(P[0],P[1])


#
# def user():
#     a1=int(input("value for a1 >"))
#     b1=int(input("value for b1>"))
#     c1=int(input("value for c1>"))
#     a2=int(input("value for a2 >"))
#     b2=int(input("value for b2>"))
#     c2=int(input("value for c2>"))
#     return a1,b1,c1,a2,b2,c2
# def solve(a1,b1,c1,a2,b2,c2):  #cramers rule
#     D=(a1*b2)-(a2*b1)
#     Dx=(c1*b2)-(c2*b1)
#     Dy=(a1*c2)-(a2*c1)
#     x=Dx/D
#     y=Dy/D
#     return x,y
# def output(x,y):
#     print(f" the value of x is {x:.2f} and y is {y:.2f}")
# a=user()
# v=solve(a[0], a[1], a[2], a[3], a[4],a[5])
# output(v[0],v[1])


def def__init__():
    pass




class Human:
    def __init__(self,fname, lname, age, state_of_origin):
        self.fname=fname
        self.name=lname
        self.age=age
        self.state_of_origin=state_of_origin
    def son(self):
        print(self.fname, self.lname, self.age, self.state_of_origin)



x=Human("John", "Born", 45,"Ondo_state")




import datetime















