#Write a python program to print all possible prime numbers from 1 to n. 
#Program:-
def fun(num): 
 count=0 
 for i in range(1,num+1): 
    count=0 
 for j in range(1,i+1): 
    if i%j==0: 
        count=count+1 
 if count==2: 
    print(i) 
num = int(input("Enter a number: ")) 
fun(num)