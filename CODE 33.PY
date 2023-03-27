#Write a python program to check whether a given number is a prime number. 
#Program:-
def fun(num): 
 count=0 
 for i in range(1,num+1): 
    if num%i==0: 
     count=count+1 
 if count==2: 
    print(num,"is a prime number.") 
 else: 
    print(num,"is not a prime number.") 
num = int(input("Enter a number: ")) 
fun(num)