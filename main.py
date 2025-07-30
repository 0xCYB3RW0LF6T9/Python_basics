print("Hello World")

# for single line cooment
'''Multi line comment'''

a="Tahmid tazowar sachya"
b="Lamar"
print("My name is "+a+" "+"My friend name is "+b)

#numeric type data
n1=475942
n2=45.53986
n3=948357935j
print(n1)
print(n1,"is a ",type(n1),"type data")
print(n2)
print(n2,"is a",type(n2),"type data")
print(n3)
print(n3,"is a",type(n3),"type data")

#boolean type data

b= True
print(type(b))

b1=87
b2=58
print("x =",b1,"y =",b2,"\n x>y",b1>b2)

#string type data
s1="Hacked by Wolf"
s2="Pwned by cyb3rw0lf"
print("I am Tahmid Tazowar Sachhya known as "+s1+" "+"Also you can say "+s2)
print("I am TAhmid Tazowar Sachhya known as",s1,"You can also say",s2)
print(f"I am Tahmid Tazowar Sachhya known as {s1} you can also say {s2}")

#Binary type data
#bytes and bytearray
l1=[4,3,4,2,3,8,7,4]
lv=bytearray(l1)

print(lv[0])

lv[0]=10

print(lv[0])

#None type data
an=None
print(an)
print(type(an))

#Llist type data = i)list(muteable) ii)Tuple(immuteable) iii)range
l1=["tahmid","udoy","Sifat"]

print(l1)
print(type(l1))
l1[0]="hacked"
print(l1)

#tuple type data ----> NO assignment/ unchangeable
l2=(2,3,54,34,342,32,3,13,)
print(l2)
print(type(l2))

#range()
x =range(10)
print(x)
for i in x:
    print(i)

#operators in python
    '''assignment , logical , conditional, arrithmetic,bitwise,identity,member '''

# Arithmetic operators
#+,-,*,/,%,**,//

a1=10
a2=20

print(a1+a2)
print(f"X={a1} y+{a2} \n x-y={a1-a2}")

print("x=",a1,"y=",a2,"\nx*y=",a1*a1)

print(a2/a1)

print(a2%a2)
a3=2
print(a1 ** a3) #a1=10 and a3=2 ==> 10*10*10+100

a4=69
print(a4//a2) #// will automatically transfer the float value in integer value
print(a4/a2)

#assignment operator

ao1=5
ao2=10
sum1=0
sum1=ao1+ao2
print(sum1)

sum1+=ao2
print(sum1)
minus=2
minus-=ao2
print(minus)

mul=5
mul**=a3
print(mul)

#Comparision operator
co=1
co2=5
gg=co==co2
print(gg)
print(co<=co2)

#swapping
x1=65
x2=100

print("Before mofication \n x1=",x1,"x2=",x2)

x1,x2 = x2,x1

print("After mofication \n x1=",x1,"x2=",x2)

#user inout

# us1=input("Enter your Username : ")
# passw=input("Enter your Password : ")
# print(us1)
# print(passw)


#type casting

tc1=35.342
print(int(tc1))
print(type(int(tc1)))

#list
li=[2,4,6,4,"Tahmid",52,4]
print(li)
print(type(li))
print(li[4])
li[4]="hacked"
print(li)
li.append("hacked")
print(li)
li.insert(0,"TAHMID TAZOWAR SACHHYA ")
print(li)

#list item delete

list1=["tahmid","udoy","Sifat","prapty","Mariya","devel","dante","hasan"]

# print(list1)
# list1.remove("udoy")
# print(list1)
#
# list1.pop(0)
# print(list1)

del list1[3]
print(list1)

list1.clear()
print(list1)

#loop list
#for loop list

lst=["tahmid","udoy","Sifat"]
for i in lst:
    print(i)

for x in range(len(lst)):
    print(x)
#while loop list
y=0
while y<len(lst):
    print(lst[y])
    y+=1

#list comprehension
nli=[4,2,4,5,6,7,3]
# for z in nli:
#      print(z)
#
double=[z*2 for z in nli]
print(double)

#list sorting

xd=[53,44,43,54,2,54,63636,3454,334,73]
print(xd)
xd.sort()
print(xd)
xd.sort(reverse=True)
print(xd)
xd1=["asd","afafer","asda","gfrgtrf","dsdtrg","rf","dsf","gh","re","w","ys","v"]
xd1.sort()
print(xd1)
xd1.sort(reverse=True)
print(xd1)

#copy list

cl1=[435,654,34,3,64,3,523,543,6,5,3,4,34,3,2,3,4,2,3,2,1,]
cl2=cl1.copy()

print(cl1)
print(cl2)


#list concat nation
#normal way
clist1=[1,2,3,4,5]
clist2=[6,7,8,9,10]
clist3=clist1+clist2
print(clist3)

#function
clist1.extend(clist2)
print(clist1)

#matrix

mat=[

    [1,2,3,4,5],    #0
    [6,7,8,9,10],   #1
    10              #2
    ]


''' [1,2,3,4,5],[6,7,8,9,10],10 '''

print(mat[0][2])

#tuple type data
t=(2,3,4,5,6,7)
print(type(t))
print(t[2])
#negative indexing
print(t[-1])
print(t[-2])

#range
print(t[0:5])

#tuple data update
ttd=(2,3,4,5,6,7)
#tuplr to list
x1=list(ttd)
print(type(x1))

x1.append("haced by cyb3rw0lf")
x1.insert(0,"test by wold")
x1.pop(3)
#changing bato to Turple
ttd=tuple(x1)
print(ttd)


#tuple can be added to new tuple

tx1=(1,2,3,4,5,6,7)
tx2=(8,9,10,11,12,13)
print(tx1+tx2)

#tuple unpacking
tu=(20,21,22,23,24)
(a,*b) = tu
print(a)
print(b)


#lopping i n tuple

s=("hacter","tesstu","laet","hex","h4ang")

for i in s:
    print(i)

#for loop using range
for x in range(len(s)):
    print(s[x])

#while loop
d=("vector","ssac","warrior")
h=0
while h<len(d):
    print(d[h])
    h+=1

#tuple join

tp1=(1,2,3,4,5)
tp2=(6,7,8,9,10)
tp3=tp1 * 2
tp4=tp1+tp2
print(tp4)
print(tp3)


#turple method
#i)indexing- find the index of any value or object
#ii)count_ find how exact many values are in the list
y=tp1.count(2)
zx=tp1.index(5)
print(y)
print(zx)



#Python set = unchangeable,only add remove available,no indexing,unordered
ps={"tahmid","udoy","Sifat","prapty","Mariya"}
print(ps)
print(type(ps))
print(len(ps))

for i in ps:
    print(i)

print("tahmid" in ps)


#set value add
#i)add --we can any thing in set such as list/dict/tuple
#ii)update
std1={1,2,3,4,5}
std2=(5,6,7,8,9,)

#add method
std1.add("Tahmid")
print(std1)

std1.update(std2)
print(std1)

#set value remove

sv1={"tahmid","udoy","Sifat","prapty"}
sv1.remove("tahmid")
print(sv1)
sv2={"hasan","hsak","flask","alu"}
sv2.discard("hasan")
print(sv2)
sv2.remove("alu")
print(sv2)
sv2.clear()
print(sv2)

#set looping only support
xx={"Tahmid","udoy","Sifat","prapty"}

for asd in xx:
    print(asd)

#set update
xxc={1,2,3,4,5}
xxc1={5,6,7,3,4,32,46,32,}
cf=xxc.union(xxc1)
print(cf)

xxc.update(xxc1)
print(xxc)


#dictonary -->changeable,indexable,ordered, duplicate not allowed
dict={
    "student_1":{
                 "name":"Tahmid Tazowar sachhya",
                 "class":"12",
                 "id":"0802510205101004",
                 "location":{

                                      "Presenet": "Nilphamari",
                                       "hometown": "Dinajpur"
                            }




                },

    "student_2":{
                "name":"CYB3Rw0LF",
                "class":"12",
                "id":"0802510205101004",
                "location":"Okland",
                "profession":"hacker"
                }

                    }

print(dict)

# print(dict["student_1"]["name"])
# print(dict["student_2"])

#dictonary access
#indexing method
print(dict["student_1"]["location"]["hometown"])

#get method

print(dict.get("student_1"))

#keys method -> only bring the parent keys
print(dict.keys())

#values method -> bring all the value in the dictionary
print(dict.values())


#dictionary data change
#indexiong method ->specific data can be updated
 #before update
print(dict["student_1"]["location"]["hometown"])
dict["student_1"]["location"]["hometown"] = "Dhaka"
#after update
print(dict["student_1"]["location"]["hometown"])

#update method - it can completly edit a key and it's all values

dict.update({"student_1":"I am here in the d4rk"})
print(dict)

#dictionary remove item:

# dict.popitem()  #delete the last key and value
# print(dict)

dict.pop("student_2")   #delete a specific kry and value
print(dict)

#if elif else condition
# te=int(input("enter your age : "))
#
# if te>18:
#     print("Voter")
# elif te<18:
#     print("non_Voter")
# else:
#     print("Not_a_valid_input")


#looping

#while loop->supports condition
k=0

while k<10:
    print(k)
    k=k+1

#for loop-only works when value is known to us

gg=("Hacked","BY","CuB3rW0LF")
for jj in gg:
    print(jj)

#function
def plus (a,b):
    c=a+b
    print(c)

def minus(x,y): #we can use same variable but it will not give us an error
    z=x-y
    print(z)

plus(2,6)
minus(2,6)

#continue and break

for i in range(10):
    if i==5:
        break
    print(i)

for j in range(10):
    if j==5:
        continue
    print(j)


#recursion - max limit 1000
# def g():
#     print("hi")
#     g()
#
# g()

#zipping

std1=("Tahmid","Tazowar","Sachhya")
std2=(1004,1006,1006)

res=list(zip(std1,std2))
print(res)


#lambda-->short form of user define function
xsw=lambda a,b : a+b

print(xsw(3,100))

##array-->it is as same as a list
arr=[1,2,3,4,5]
print(arr)

class t:
    name=""
    id=""
    number=""

a= t
a.name="Tahmid"
a.id="0802510205101004"
a.number="32493493824"
print(a.name)
print(a.id)
print(a.number)

#Inheritance

class y(t):
    name=""

z=y()
y.name="Tazowar"
y.id="3454"
y.number="23"
print(y.name)
print(y.id)
print(y.number)

#multiple_inheritance
class x:
    games = ""
    player = ""
class y:
    name=""
    id=""
    number=""

class z(x,y):
     count=""


c=z()
c.name="hacked"                     #from  y
c.games="Legend of Zelda"           #from  x
c.count="100"                       #from  z

print(c.games)
print(c.name)
print(c.count)

#multi_level_inheritance
class x:
    games = ""
    player = ""
class y(x):
    name=""
    id=""
    number=""

class z(y):
     count=""


xsd=z()
xsd.name="hacked"
xsd.games=" Grid Autosport"
xsd.count="100"
print(xsd.games)
print(xsd.name)
print(xsd.count)


#iterator

cc=(1,3,5,4,2,3,"tahmid","tahz","Hsana")
# for sha in cc:
#     print(sha)

xfa=iter(cc)
print(xfa.__next__())
# we can use two different functions for iteration
# i)print(varibale_name . __next__()
# ii) print(next(x))
print(next(xfa))
print(next(xfa))
print(next(xfa))
print(next(xfa))
print(xfa.__next__())


#scoping => local and global variable
dsa=100 #global variable
def twst():
    print(dsa)  #acceesssing global variable
    dsa1=60 #local variable for twst
    print(dsa1)



twst()

#trying to print the local variable from outside
#print(dsa1)
# #we will get a error


#DAte
import datetime
xfb=datetime.datetime.now()

print(xfb.strftime("MOnth= %B  year= %Y day =%A  time= %I:%M"))


# math function
 #max,min,abs,pow
asw=min(234,24,12,34,245,6,5,6,5,4,56,7)
print(asw)
asw1=max(234,24,12,34,245,6,5,6,5,4,56,7)
print(asw1)

asw2= abs(-1246) #converts negative integer into positive

print(asw2)

asw3=pow(2,3)
print(asw3)


#Regular Function
import re
txt="Test by wolf id is 0802510205101004"

x=re.findall("w...",txt)
print(x)
if x:
    print("Available")

else:
    print("Not Available")


#try and accept
try:
    print("Hacked_by_CYRYS")
except:
    print(x)
print("Hacked_by_CYRYS1")
print("Hacked_by_CYRYS2")

print("rfwiu")

#file read
ssd1212=open("g.txt","r")
print(ssd1212.read())


#file read

gif=open("h.txt","a")
hex=gif.write("This is Tahmid Tazowar Sachhya ")
print(hex)


#file remove
#import os
#file delete
#os.remove("h.txt")
#folder delete
#os.rmdir("File_name")



#creating own modules -->i)import file_name (without extinction) ii)import file_name (without extinction) as name
# iii)from file_name  import function
import t3

f=t3.y
print(f)


a=t3.x(5,3)

b=t3.t
b.name="Hacker"
b.id="0802510205101004"

print(b.name,"\n",b.id)

'''Python OOP
	1.class and order
	2.inheritance
	3.abstraction 
	4.encapsulation
	5.polymorphisiom 
'''''

#constructor

class fx:
    def tuu(self,a,b):
        print(f"I am {a} and i am {b} years old ")

    def __init__(self, a, b):
        print(f"I am {a} and i am {b} years old ")



yxd=fx("Cyb3Rw0lf",19)
xha=fx("virus",291882)
cdf=fx()
cdf.tuu(10,20)

























