def func(str, i=0):
 if i == len(str): 
    print("".join(str))
 for j in range(i, len(str)):
    chars = [c for c in str]
    chars[i], chars[j] = chars[j], chars[i] 
    func(chars, i + 1)
str=input("Enter a string")
print(func(str))