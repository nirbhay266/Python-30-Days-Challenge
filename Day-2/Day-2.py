x=5
y="Nirbhay"
c=3.14
print(x)
print(y)
print(x,y,c)
print(f"My name is  {x} and you age is {x}")

print(type(y))
print(type(x))
print(type(c))

####################################################### INTEGER ###################################################
age=25
family=6
brother=2
print("my age is",age)
print(f"my age is {age}")
print("member of in my family",family)
print(f"In my family {family}th members")
print(f"I have {brother} brothers")

print(type(age))

#Casting

print(float(age))
print(float(family))
print(float(brother))


#################################################### FLOAT ##########################################################
cgpa=8.5
percentage=80.2
distance=5.5
print("My CGPA in BCA is ",cgpa)
print(f"My CGPA in BCA is {cgpa}")
print("my 12th marks are",percentage)
print(f"My 12th marks are {percentage}%")
print(f"My college is {distance} km away from my home")

print(type(cgpa))
print(type(percentage))

#Casting
print(int(cgpa))
print(int(percentage))
print(int(distance))


##################################################### STRING #######################################################
fname="Nirbhay"
mname='Kumar'
lname='Yadav"'
print(fname)
print(mname)
print(lname)

print(fname,"",mname,"",lname)
print(fname+"",mname+""+lname)

a=""""Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""
print(a)

a='''"Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.'''
print(a)

Item="biscate"
price=80
Quantity=5

print(f"I want Purchase {Item}")
print(f"The {Item} price is {price:2f}$")
print(f"I want purchase {Quantity} {Item}")
print(f"Total Cost of {Item} {price*Quantity}$")

name="Nirbhay"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[0],name[1],name[2],name[3],name[4],name[5],name[6])


name="Nirbhay kumar"
print(name[2:5])
print(name[:5])
print(name[2:])

fname,mname,lname="Nirbhay","Kumar","Yadav"
print(fname)
print(mname)
print(lname)

x = y = z = "Orange" 
print(x) 
print(y) 
print(z)
#################################################  Booleans ######################################################
age=18
print(age>18)
print(age>=18)

print(10>11)
print(20>10)

if age>18:
    print("Yes age is greater than 18 ")
else:
    print("No age is less than 18 ")




