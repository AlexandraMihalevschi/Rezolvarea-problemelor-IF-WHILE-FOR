n = eval(input("Dati numarul: "))
s1 = 0
c = 0
v = 0
s2a = 0

for n in range(1, n+1):
    c+=n
    s1+=n**3
    v+=n**2
    s2a=(n**3)+(n**2)+c

s2 = c**2
s1a = 3*v

if s1>s2:
    print(s1)
elif s1<s2:
    print(s2)
elif s1==s2:
    print(s1, "=", s2)

if s1a>s2a:
    print(s1a)
elif s1a<s2a:
    print(s2a)
elif s1a==s2a:
    print(s1a, "=", s2a)