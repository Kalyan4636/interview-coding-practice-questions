def func(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in str:
            return False
        return True
str = input("Enter a string")
str=str.lower()
res=func(str)
if(res==True):
 print("The string is pangram.")
else:
 print("The string is not a pangram.")