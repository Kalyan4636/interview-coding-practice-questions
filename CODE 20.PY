# Write a python program to find the duplicate element present in an array. 
#Program:-
arr = [10,20,30,40,20,40,50,30,60,70,80]; 
print("Duplicate elements in given array: "); 
for i in range(0, len(arr)): 
 for j in range(i+1, len(arr)): 
    if(arr[i] == arr[j]): 
        print(arr[j])