# Write a python program to print the unique values present in a dictionary. 
#Program:-
dict = {'KodNest':[10,20,30,40],'is':[10,50,30,60],'awesome':[20,70,80,90]} 
print("The original dictionary is : " + str(dict)) 
res = list(sorted({ele for val in dict.values() for ele in val})) 
print("The unique values list is : " + str(res))