# Write a python program to print the factorial of a given number. 
#Program:-
num = int(input("Enter a number: ")) 
fact = 1 
if num < 0:
 print("Kindly enter the positive number") 
elif num == 0: 
 print("The factorial of 0 is 1") 
else: 
 for i in range(1,num + 1): 
    fact = fact*i 
 print("The factorial of",num,"is",fact)