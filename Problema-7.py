n = int(input("Ce varsta are Mihai: "))
s = 1
if (n<20)and(n>=0):
    for n in range(1, n+1):
        s=(s*2)+n
    if (s>100)and(n!=6):
        print("La varsta de", n, "ani, suma era deja mai mare de 100$, incepand cu a 6-a aniversare")
    else: print("La varsta de", n, "ani, Mihai avea mai mult de 100$")
    print("Suma totala primita este", s, "$")
else: print("Mihai este deja prea mare sa primeasca bani de la unchi")

