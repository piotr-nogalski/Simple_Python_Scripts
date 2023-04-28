import random
import time


arr = []
count = 1


for i in range(0, 500):
    arr.append(random.randrange(0, 15))

print(arr)
start = time.time()
while count:
    count = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count = 1
end = time.time()
print(arr)
print("Sorting time:", round(end - start, 2))
