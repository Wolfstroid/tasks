import random

def insert_sort(arr):
    for n in range(len(arr)):
        m = 0
        while m < n:
            if arr[len(arr)-1] <= arr[m]:
                arr.insert(m,arr[len(arr)-1])
                arr.pop()
                break
            elif m is n-1:
                arr.insert(n,arr[len(arr)-1])
                arr.pop()
                break
            m = m + 1
    return arr

arr = []
for n in range(100):
    arr.append(random.randint(0,1000))
print("before:")
print(arr)
insert_sort(arr)
print("after:")
print(arr)

