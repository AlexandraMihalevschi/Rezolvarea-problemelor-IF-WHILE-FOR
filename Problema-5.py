n = int(input("Anul nasterii: "))
if n%12==8:
    print("Dragon")
elif n%12==9:
    print("Sarpe")
elif n%12==10:
    print("Cal")
elif n%12==11:
    print("Oaie")
elif n%12==0:
    print("Maimuta")
elif n%12==1:
    print("Cocos")
elif n%12==2:
    print("Caine")
elif n%12==3:
    print("Porc")
elif n%12==4:
    print("Sobolan")
elif n%12==5:
    print("Bou")
elif n%12==6:
    print("Tigru")
elif n%11==7:
    print("Iepure")
else: print("Dati un an exprimat prin cifre")