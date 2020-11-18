m = int(input("Dati un numar pentru baza: "))
n = int(input("Dati un numar pentru putere: ")) 
if n<m:
    print("Introduceti alte numere")
elif m==1:
    print("n este o putere a lui m, egala cu 1")
if m<n:
    i=0
    while n%m==0:
        n=n/m
        i+=1
    print("m la puterea", i,"= n","n poate fi o putere al lui m")