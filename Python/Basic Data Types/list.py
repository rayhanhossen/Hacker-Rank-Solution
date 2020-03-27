n = int(input())
list = []
for n in range(n):
    x = input().split()
    command = x[0]
    if command == 'append':
        list.append(int(x[1]))
    if command == 'print':
        print(list)
    if command == 'insert':
        list.insert(int(x[1]), int(x[2]))
    if command == 'reverse':
        list.reverse()
    if command == 'pop':
        list.pop()
    if command == 'sort':
        list.sort()
    if command == 'remove':
        list.remove(int(x[1]))