import math
n = int(input("Dati numarul: "))
s = 0
for n in range (1,n+1):
    s = s + math.factorial(n)

print("Suma factorialilor este", s)