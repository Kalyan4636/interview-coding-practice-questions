#Write a python program to reverse a string. 
#Program:-
def fun(str): 
 str1 = "" 
 for i in str: 
    str1 = i + str1 
 return str1 
str = input("Enter a string :") 
revstr=fun(str) 
print("The original string is: ",str) 
print("The reverse string is",revstr)