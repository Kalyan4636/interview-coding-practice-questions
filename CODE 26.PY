#Write a python program to print the Fibonacci series till n. 
#Program:-
n = int(input ("Enter value of n:")) 
n1 = 0 
n2 = 1 
count = 0 
if n<=0: 
 print ("Please enter a positive integer.") 
elif n==1: 
 print ("The Fibonacci sequence of the numbers up to", n, ": ") 
 print(n1) 
else: 
 print ("The fibonacci sequence of the numbers is:") 
 while count<n: 
    print(n1) 
 n3 = n1 + n2 
 n1 = n2 
 n2 = n3 
 count = count+1