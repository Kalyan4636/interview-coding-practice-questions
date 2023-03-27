#Write a python program to copy all elements of one array into another array. 
#Program:-
arr1 = [10, 20, 30, 40, 50]; 
arr2 = [None] * len(arr1); 
for i in range(0, len(arr1)): 
 arr2[i] = arr1[i]; 
print("Elements of original array: "); 
for i in range(0, len(arr1)): 
 print(arr1[i]), 
print(); 
print("Elements of new array: "); 
for i in range(0, len(arr2)): 
 print(arr2[i]),