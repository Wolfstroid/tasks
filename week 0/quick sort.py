import random

def quick_sort(arr):
    if len(arr) <= 2:
        return arr
    else:
        i,j = 1,len(arr)-1
        while i != j:
                if arr[j] < arr[0]:
                    arr[j],arr[0] = arr[0],arr[j]
                    break
                j = j - 1 
        while i != j:
            while i != j:
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
                i = i + 1 
            while i != j:
                if arr[j] < arr[i]:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
                j = j - 1 
        l1 = quick_sort(arr[:i])
        l2 = quick_sort(arr[i-len(arr):])
        return l1 + l2


arr,afterarr = [],[]
for n in range(100):
    arr.append(random.randint(0,1000))
print("before:")
print(arr)
after_arr = quick_sort(arr)
print("after:")
print(after_arr)
