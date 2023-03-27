#Write a python program to swap two numbers. 
#Program:-
x=int(input("Enter the first number")) 
y=int(input("Enter the second number")) 
print("The numbers before swapping are:",x,y) 
temp = x 
x = y 
y = temp 
print("The numbers after swapping are:",x,y)