import math

def binary(arr, leastval, arrsize, sval):
    if arrsize >= leastval:
        mid = math.ceil(leastval + (arrsize - leastval) / 2)
        if arr[mid] == sval:
            return mid

        elif arr[mid] > sval:
            return binary(arr, leastval, mid - 1, sval)

        else:
            return binary(arr, mid + 1, arrsize, sval)

    else:
        return 'invalid'

def Binarysearch(array,lval,size,string):
    if binary(array,lval,size,string) != 'invalid':
        validation = 'valid'
        return validation
    else:
        validation = binary(array,lval,size,string)
        return validation





