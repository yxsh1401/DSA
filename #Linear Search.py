#Linear Search
def linear_search(arr,n,x):
    for i in range(0,n):
        if (arr[i] == x):
            return i
    return -1

arr = [1,2,3,4,5]
n = len(arr)
x = input(int("Enter the number to be searched"))
result = linear_search(arr,n,x)
print
 