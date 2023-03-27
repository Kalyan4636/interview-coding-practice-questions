# Write a python program to find the H.C.F. of two numbers. 
#Program:-
def hcf(num1, num2): 
 if num1>num2: 
    smaller = num2 
 else: 
    smaller = num1 
 for i in range(1,smaller + 1): 
    if((num1 % i == 0) and (num2 % i == 0)): 
        hcf = i 
 return hcf 
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))