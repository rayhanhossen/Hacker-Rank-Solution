if __name__ == '__main__':
    n = int(input())

    if n%2 == 0:
        if ((n>=2 and n<=5) or n>20):
            print("Not Weird\n")
        elif (n>=6 and n<=20):
            print("Weird\n")
    else:
        print ("Weird\n")
