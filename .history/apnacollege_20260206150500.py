print("hello python")
s=1444
print(s)

name = "sneha gupta"
age = 19
height = 5.5
age2 = age

print(age)
print(name)

print("my height is : ", height)
print(age2)

print(type(age))
print(type(name))
print(type(height))

c = None
old = True
print(type(c))
print(type(old))

s = 1200
v = 120
sum = s+ v
diff = s - v
print(sum)
print(diff)
print(s*v)
print(v/s)
print(s/v)
print(s%v)
print(s== v) #False
print(s!= v) #True
print(s>v) #True
#this is my first python code

"""
hey hehehehhee
"""
#logical operator
print(not False) # True
print(not True) # False

val1 = True
val2 = False
print("AND operator :", val1 and val2) #False
print("OR operator :", val1 or val2) #True

#type conversion
a = 2
b = 4.45
sum  = a + b # 2.0 + 4.45 => 6.45
print(sum) #6.45 implicit type conversion

d = "3"
#print(a + d) #explicit type conversion 
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
e = int(d)
print(a+ e)#type casting
#result of a + e =  5

name = input("enter some values : ")
print(type(val), value)
