#-is used to comment single line in python.
#Data types in Python:
#int Data Type:
a=10
print(a)#10
print(type(a))#int
#int is used to store integer type of real world data.

#float Data Type:
b=10.78482
print(b)#10.78482
print(type(b))#float
#float is used to store real numbers.

#bool Data Type:
c=True
print(c)#True
print(type(c))#bool
#bool Data type is used to store True/False.

#str Data Type:
d="aditya"
print(d)#aditya
print(type(d))#str
#for single char and series of characters the data type is str only.

#complex Data Type:
e=5+6j
print(e)#(5+6j)
print(type(e))#complex
#complex data type is used to store complex numbers.
'''Whenever we are performing division in python result will always in
float datatype as shown above:'''


#Performing type casting on integer:
'''
• int-float-float( ) • int-str-str( ) • int-bool
• int-complex
'''

#int-float :yes we can perform
a=10
print(a)#10
print(type(a))#int
b=float(a)
print(b)#10.0
print(type(b))#float'''

#int-str -yes we can perform
a=10
print(a)#10
print(type(a))#int
b=str(a)
print(b)#10
print(type(b))#str'''
#int-bool yes we can perform

#for all non-zero values output will be True.
#for a=0 only we will get output False.
a=10
print(a)#10
print(type(a))#int
b=bool(a)
print(b)#True
print(type(b))#bool'''

#int-complex yes we can perform
#for 0 we will get output as 0j not as 0+0j
a=10
print(a)#10
print(type(a))#int
b=complex(a)
print(b)#(10+0j)
print(type(b))#complex'''
