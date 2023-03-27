#Write a python program to find the L.C.M. of two numbers. 
#Program:-
def lcm(num1, num2): 
 if num1 > num2: 
    greater = num1 
 else: 
    greater = num2 
 while(True): 
    if((greater % num1 == 0) and (greater % num2 == 0)): 
        lcm = greater 
 break 
 greater = greater+1 
 return lcm 
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))