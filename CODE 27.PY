#Write a python program to print the multiplication table of a given number. 
#Program:-
num = int(input ("Enter the number to print the multiplication table: ")) 
print ("The Multiplication Table of: ", num) 
for i in range(1, 11): 
 print (num, 'x', i, '=', num*i)