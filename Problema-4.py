from fractions import Fraction
a = int(input("Numaratorul primei fractii: "))
b = int(input("Numitorul primei fractii: "))
c = int(input("Numaratorul fractiei a 2-a: "))
d = int(input("Numitorul fractiei a 2-a: "))
print("Suma celor 2 fractii este", Fraction(a,b)+Fraction(c, d))
print("Produsul celor 2 fractii este", Fraction(a,b)*Fraction(c, d))