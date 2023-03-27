# Write a python program to print the average of the marks for the student up to 2 places after the decimal. 
#Note: You are given a dictionary containing the {name : marks} for students. You have to 
#find the average marks for a student name provided.
#Input Format:
#The first line contains the integer n, the number of students’s records. 
#The next n lines contain the names and marks obtained by a student, each value separated by a space. 
#The final line contains the name of a student for which average should be printed.
#Output Format:
#Print the average of the marks obtained by the particular student up to 2 decimal places.
#Sample Input:
#Enter the number of students 3
#Enter the name and marks for students Rahul 40 50 60
#Enter the name and marks for students Mohan 50 60 70
#Enter the name and marks for students Simran 60 70 80
#Enter the name of student to display the average Mohan
#Sample Output: 60.00
#Program:-
n = int(input("Enter the number of students"))
students = {}
for _ in range(n):
 name, *line = input("Enter the name and marks for students").split()
 scores = list(map(float, line))
 students[name] = scores
 
student_name = input("Enter the name of student to display the average")
output = list(students[Mohan]) 
per = sum(output)/len(output);
print("%.2f" % per);