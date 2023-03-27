#Write a python program to swap two numbers without using a third variable. 
#Program:-
x=int(input("Enter the first number")) 
y=int(input("Enter the second number"))
print("The numbers before swapping are:",x,y) 
x=x+y; 
y=x-y; 
x=x-y; 
print("The numbers after swapping are:",x,y)