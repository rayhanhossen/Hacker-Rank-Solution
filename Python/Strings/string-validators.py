def validator(s):
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(ele) for ele in s))

if __name__ == '__main__':
    s = input()
    validator(s)
