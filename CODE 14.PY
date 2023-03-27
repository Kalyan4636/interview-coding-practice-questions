# Write a python program to remove the punctuations in a given string. 
#Program:-
punctuation_var = '''''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
str = input("Enter a string: ") 
no_punctuation_str = "" 
for i in str: 
 if i not in punctuation_var: 
    no_punctuation_str = no_punctuation_str + i 
print(no_punctuation_str)