#Write a python program to find the sum of all the values in a given dictionary. 
#Program:-
def fun(dict): 
 list = [] 
 for i in dict: 
    list.append(dict[i]) 
 final = sum(list) 
 return final 
dict = {'x': 10, 'y': 20, 'z': 30} 
res=fun(dict) 
print("The sum of all values in the dictionary",dict,"is: ", res)