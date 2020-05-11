import numpy

def arrays(arr):
    np = numpy.array(arr, float)
    return np[::-1]
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)