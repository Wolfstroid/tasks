import random

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        l1 = merge_sort(arr[:len(arr)//2])
        l2 = merge_sort(arr[len(arr)//2-len(arr):])
        l3 = []
        while len(l1) and len(l2):
            if l1[0] <= l2[0]:
                l3.append(l1[0])
                l1.pop(0)
            else:
                l3.append(l2[0])
                l2.pop(0)
        l3 = l3 + l1 + l2
        return l3

arr,after_arr = [],[]
for n in range(100):
    arr.append(random.randint(0,1000))
print("before:")
print(arr)
after_arr = merge_sort(arr)
print("after:")
print(after_arr)