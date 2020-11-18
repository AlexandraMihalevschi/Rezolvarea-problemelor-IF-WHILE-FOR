n = eval(input("Dati numarul: "))
s1 = 0
c = 0
v = 0
s2a = 0
k = 0

for n in range(1, n+1):
    c+=n
    s1+=n**3
    v+=n**2
    k+=n**n
    
s2 = c**2
s1a = 3*v
s2a = k+c

if s1>s2:
    print("Mai mare este prima suma:", s1)
elif s1<s2:
    print("Mai mare este a doua suma:", s2)
elif s1==s2:
    print(s1, "=", s2)

if s1a>s2a:
    print("Mai mare este prima suma:", s1a)
elif s1a<s2a:
    print("Mai mare este a doua suma:", s2a)
elif s1a==s2a:
    print(s1a, "=", s2a)