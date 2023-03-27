str1 = input("Enter first string")
str2 = input("Enter second string")
str1 = str1.lower()
str2 = str2.lower()
if(len(str1) == len(str2)):
 str1_sorted = sorted(str1)
 str2_sorted = sorted(str2)
 if(str1_sorted == str2_sorted):
    print(str1 + " and " + str2 + " are anagram.")
 else:
    print(str1 + " and " + str2 + " are not anagram.")
else:
 print(str1 + " and " + str2 + " are not anagram.")