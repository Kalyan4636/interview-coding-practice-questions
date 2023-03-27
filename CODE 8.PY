#Write a python program to sort the words in a given string.
#Program:-
str = input("Enter a string: ") 
words = str.split() 
words.sort() 
for word in words: 
 print(word)