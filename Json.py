#JSON(Java script object notation)
#it is used for storing and exchanging data. it is used to store data in database
# it is similar to python dict.

#Json                                               #pythom
#null                                                 #None
#True                                                   #True
#False                                                  #False
#ascii
#Uft-8 encode

import json
import webbrowser

a=dir(json)
print(a)

#load(object), loads(string), dump, dumps
#keys methods
#json.load(f):load json data from fithe(or file-like object)
#json.loads(f): Load json data from a string.
#json.dump(j,f): write json object to the file(or file-like object)
#json.dumps(j): output json object as string.


#{"tithe": "Gattara", "relaese_year": 1997, "is_awesome":true, "won_oscar": false,
# "actor":["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"],
# "budget": null,
# "credits": {"director": "Andrew Niccol",
           # "writer": "Andrew Niccol",
           # "Composer": "Micheal Nyman",
           # "Cinematographer": " Stawomir idziak"}}
#using json.load
Json_file=open("C:\\Users\\user\\tithe.txt", "r", encoding="utf-8")
movie=json.load(Json_file)
Json_file.close()
# print(movie)
# print(type(movie))

value='''
{"title": "Tron : legacy",
          "composer": "Duff Punk",
          "Release_Year" : 2010,
          "Budget" : 170000000,
          "Actor" : null,
          "Won_Oscar" : false}
          '''
tron=json.loads(value)
print(tron)

a=json.dumps(value)
print(a)
b=json.dumps(value, ensure_ascii=False)
print(b)

c=json.loads(b)
print(c)

#creating a file(x, w, a)
#a=open("C:\\Users\\user\\Desktop\\Valentine.txt",'x')
#print(a)
# b=open("C:\\Users\\user\\Desktop\\Valentine.txt",'w')
# b.write("Welcome to python")
# b.close()

import os
#os.remove("C:\\Users\\user\\Desktop\\Valentine.txt")
if os.path.exists("C:\\Users\\user\\Desktop\\Valentine.txt"):
    os.remove("C:\\Users\\user\\Desktop\\Valentine.txt")
else:
    print("The file does not exist")

import random
import urllib.request

#def download_image(url):
   # name=random.randrange(1,1000)
    #file_name=str(name) + ".png"
    #urllib.request.urlretrieve(url, file_name)
#download_image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

#Request module


import requests
x=requests.get("https://w3schools.com/python/demopage.htm")
print(x.text)

x="https://w3schools.com/python/demopage.htm"
v={"key": "value1"}
x=requests.post(x,data=v)
print(x)

# try:
#     # print(z)
# except:
#     print("undefined variables")

try:
    a="Ayokunle"
    b=1
    print(a +b)
except TypeError:
    print("can nor concatnate a str and int")
finally :
    print("I tire !!!")


#finally

import urllib.request
get_facebook=urllib.request.urlopen("website url")


#u
webbrowser.open()





