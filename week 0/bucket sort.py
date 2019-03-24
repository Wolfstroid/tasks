import random

# n to m sort  <type'int'>
def bucket_sort(arr):
    bucket = [0] * (max(arr) - min(arr) + 1)
    for number in arr:
        bucket[number - min(arr)] += 1
    after_arr = []
    n = 0
    while n < len(bucket):
        while bucket[n]:
            after_arr.append(min(arr) + n)
            bucket[n] -= 1
        n += 1
    return after_arr

arr = []
for n in range(100):
    arr.append(random.randint(0,1000))
print("before: ")
print(arr)
arr = bucket_sort(arr)
print("after: ")
print(arr)

