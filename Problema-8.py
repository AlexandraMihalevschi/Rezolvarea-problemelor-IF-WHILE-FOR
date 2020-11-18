a = int(input("Dati primul numar: "))
b = int(input("Dati al doilea numar: "))
c = int(input("Dati al treilea numar: "))
if (a<b+c)and(b<a+c)and(c<a+b)and(a>0)and(b>0)and(c>0):
    if (a==b)and(b==c)and(a==c):
        print("Triunghiul este echilateral")
    elif (a==b)and(a!=c)and(b!=c)or(b==c)and(b!=a)and(c!=a)or(a==c)and(a!=b)and(c!=b):
        print("Triunghiul este isoscel")
    elif (a!=b)and(b!=c)and(a!=c):
        print("Triunghiul este scalen")
else : print("Nu exista astfel de triunghi")