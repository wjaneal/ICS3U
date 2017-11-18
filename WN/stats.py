from math import *

def test_sigma(n1,n2,s1,s2):
    return sqrt((n1*s1**2+n2*s2**2)/(n1+n2-2))*sqrt((n1+n2)/(n1*n2))

def Gc(Ns, Nd):
    return 1.0*(Ns-Nd)/(Ns+Nd)

def Ns(A, B, D, E, F, H, I):
    a = A*(E+F+H+I)
    b = B*(F+I)
    c = D*(H+I)
    d = E*(I)
    print(a,b,d,c,a+b+c+d)
    return A*(E+F+H+I)+B*(F+I)+D*(H+I)+E*(I)

def Nd(B, C, D, E, F, G, H):
    a = C*(D+E+G+H)
    b = B*(D+G)
    c = F*(G+H)
    d = E*G
    print(a,b,c,d,a+b+c+d)
    return C*(D+E+G+H)+B*(D+G)+F*(G+H)+E*(G)

def calc_G(A,B,C,D,E,F,G,H,I):
    print ("Ns: ", Ns(A,B,D,E,F,H,I))
    print ("Nd: ", Nd(B,C,D,E,F,H,I))
    return Gc(Ns(A,B,D,E,F,H,I),Nd(B,C,D,E,F,G,H))

def chi_squared(A,B,C,D,E,F,G,H,I):
    R1 = A+B+C
    R2 = D+E+F
    R3 = G+H+I
    C1 = A+D+G
    C2 = B+E+H
    C3 = C+F+I
    N = (A+B+C+D+E+F+G+H+I)*1.0
    fo = (A,B,C,D,E,F,G,H,I)
    fe = (R1*C1/N,R1*C2/N,R1*C3/N,R2*C1/N,R2*C2/N,R2*C3/N,R3*C1/N,R3*C2/N,R3*C3/N)
    total = 0
    fofe = []
    fofe_squared = []
    fofe_squared_fe = []
    for i in range(0,len(fo)):
        fofe.append(fo[i]-fe[i])
        fofe_squared.append((fo[i]-fe[i])**2)
        fofe_squared_fe.append((fo[i]-fe[i])**2/fe[i])
    for i in range(0,len(fofe_squared)):
            total+=fofe_squared_fe[i]
    print(fo,fe,fofe,fofe_squared,fofe_squared_fe)
    return total


print (test_sigma(12,13,1.534, 1.487))

print (calc_G(26,7,6,14,16,22,6,28,15))
print (chi_squared(1,2,3,4,5,6,7,8,9))
