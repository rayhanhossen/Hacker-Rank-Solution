n = int(input())
list = []
for n in range(n):
    x = input().split()
    command = x[0]
    if command == 'append':
        list.append(int(x[1]))
    elif command == 'print':
        print(list)
    elif command == 'insert':
        list.insert(int(x[1]), int(x[2]))
    elif command == 'reverse':
        list.reverse()
    elif command == 'pop':
        list.pop()
    elif command == 'sort':
        list.sort()
    else:
        list.remove(int(x[1]))