import time

start = time.time()

n = int(input("Enter number to be factorized:"))
factors = []
i = 2
while n > 1:
    if n % i == 0:
        factors.append(i)
        n = n // i
    else:
        i = i + 1

end = time.time()
print(factors)
print((end-start), "seconds taken")
