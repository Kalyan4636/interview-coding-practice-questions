#Write a python program to check whether a given number is even or odd. 
#Program:-
def fun(num): 
 if num%2 == 0: 
    print(num,"is even number") 
 else: 
    print(num,"is odd number") 
num = int(input("Enter a number: ")) 
fun(num)