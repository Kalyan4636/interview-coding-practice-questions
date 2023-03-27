# Write a python program to convert a list into a string. 
#Program:-
def fun(list1): 
 str = '' 
 for i in list1: 
    str += i 
 return str 
list1 = ["Welcome","To", "CODING","Technologies"] 
s=fun(list1) 
print(s) 
print(type(s))