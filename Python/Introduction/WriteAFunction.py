def is_leap(year):
    if (year%400 ==0 or year%100 != 0 and year%4 == 0):
        year = True
    else:
        year = False

    return year

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))