#Write a python program to check whether a string can become palindrome by rearranging it or not.
#Program:-
alphabets = 256
def func(str) :
 count=[0]*(alphabets) 
 for i in range( 0, len(str)) : 
    count[ord(str[i])] = count[ord(str[i])] + 1
 num = 0 
 for i in range(0, alphabets ) : 
    if (count[i] & 1) : 
        num = num + 1
 if (num > 1) : 
    return False 
 return True
str=input("Enter a string")
res=func(str)
if(res==True): 
 print("Yes") 
else : 
 print("No")