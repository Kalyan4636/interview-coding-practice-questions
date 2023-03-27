# Write a python program to find the largest element in an array. 
#Program:-
def fun(arr,length): 
 max = arr[0] 
 for i in range(1, length): 
    if arr[i] > max: 
        max = arr[i] 
 return max 
arr = [45, 55, 75, 85, 35] 
length = len(arr) 
res = fun(arr,length) 
print("The largest number present in given array is",res)