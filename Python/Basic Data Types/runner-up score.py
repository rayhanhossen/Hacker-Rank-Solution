n = int(input())
arr = list(map(int, input().split()))[:n]

maximum = max(arr)
for i in range(n):
    if maximum == max(arr):
        arr.remove(max(arr))
print(max(arr))