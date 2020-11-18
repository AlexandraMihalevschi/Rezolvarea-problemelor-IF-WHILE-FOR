n = int(input("Dati numarul: "))
for i in range(1, n+1):
    s = 0
    d = 1
    for d in range(1, i):
        if not i%d:
            s+=d
    if s==i:
        print(i, "este un numar perfect")