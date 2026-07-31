import math

x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0

for i in range(0, n + 1, 2):
    fact = math.factorial(i)
    
    if (i // 2) % 2 == 0:
        sum = sum + (x ** i) / fact
    else:
        sum = sum - (x ** i) / fact

print("Cosine =", sum)
