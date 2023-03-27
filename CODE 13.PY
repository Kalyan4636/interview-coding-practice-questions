#Write a python program to remove a specific index character in a string. 
#Program:-
str1 = input("Enter a string:") 
index=int(input("Enter the index of a character to remove")) 
str2 = "" 
for i in range(len(str1)): 
 if i!= index: 
    str2 = str2 + str1[i] 
print ("The original string is : " + str1) 
print ("The string after removal of",index,"character : " + str2)