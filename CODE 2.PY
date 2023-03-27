print("Enter the number of scores:")
n = int(input())
arr = map(int, input("Enter the scores: ").split())
print("The runner-up score is:",sorted(list(set(arr)))[-2])