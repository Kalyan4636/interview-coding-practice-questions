#Write a python program to elements present in an array in reverse order. 
#Program:-
arr = [10, 20, 30, 40, 50] 
print("Original array: ") 
for i in range(0, len(arr)): 
 print(arr[i],end=' ') 
print() 
print("Array in reverse order: ")
for i in range(len(arr)-1, -1, -1): 
 print(arr[i],end=' ')