#Write a python program to sort an array in an ascending order. 
#Program:-
arr = [100,50,150,25,125,75,175]
temp = 0
print("Elements of original array: ")
for i in range(0, len(arr)): 
 print(arr[i], end=" ");
for i in range(0, len(arr)): 
 for j in range(i+1, len(arr)): 
    if(arr[i] > arr[j]): 
        temp = arr[i]
 arr[i] = arr[j] 
 arr[j] = temp
print() 
print("Elements of array sorted in ascending order: ")
for i in range(0, len(arr)): 
 print(arr[i], end=" ")