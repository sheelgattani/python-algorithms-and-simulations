import time

def recursivefibo(num1, num2, count):
    if count == 0:
        return 
    print(num1)
    recursivefibo(num2, num1+num2, count - 1)

def iterativefibo(count):
    i = 1
    a = 0
    b = 1
    while i <= count:
        print(a)
        a, b = b, a+b
        i += 1
    
n = int(input("Enter number of terms in fibonacci sequence:"))

while True:
    choice = int(input("Enter 1 for recursive or 2 for iterative:"))
    if choice == 1:
        start = time.time()
        recursivefibo(0, 1, n)
        end = time.time()
        print((end-start), "seconds taken")
        break
    elif choice == 2:
        start = time.time()
        iterativefibo(n)
        end = time.time()
        print((end-start), "seconds taken")
        break
    else:
        print("Try again")
