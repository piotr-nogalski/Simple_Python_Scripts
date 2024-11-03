import random
import time


var = []
count = 1


for i in range(0, 500):
    var.append(random.randrange(0, 15))

print(var)
start = time.time()
while count:
    count = 0
    for i in range(0, len(var)-1):
        if var[i] > var[i+1]:
            var[i], var[i+1] = var[i+1], var[i]
            count = 1
stop = time.time()
print(var)
print("Sorting time:", round(stop - start, 2))
