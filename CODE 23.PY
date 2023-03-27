#Write a python program to find the sum of all elements present in an array. 
#Program:-
def fun(arr): 
 sum=0 
 for i in arr: 
    sum = sum + i 
 return(sum) 
arr=[] 
arr = [10,20,30,40,50] 
n = len(arr)
res = fun(arr) 
print ('The sum of the elements present in the array is', res)