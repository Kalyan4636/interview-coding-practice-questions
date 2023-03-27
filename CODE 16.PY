#Write a python program to check whether a given string is palindrome or not. 
#Program:-
def fun(str): 
 for i in range(0, int(len(str)/2)): 
    if str[i] != str[len(str)-i-1]: 
        return False 
 return True 
str = input("Enter a string :") 
res = fun(str) 
if res==True: 
 print(str,"is palindrome.") 
else: 
 print(str,"is not a palindrome")