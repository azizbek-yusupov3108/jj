# 1

def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(1, 2, 3, 4))
print(kopaytma(5, 6))
print(kopaytma(7))

# 2

def kvadratlar(son1, son2, son3, *qolgan_sonlar):
    kvadratlar_royhati = [son1**2, son2**2, son3**2]

    for son in qolgan_sonlar:
        kvadratlar_royhati.append(son**2)

    return kvadratlar_royhati


result = kvadratlar(9, 3, 3, 4, 5, 6)
print(result)

# 3

def talaba_malumotlari(isim, familiya, **qolgan_malumotlar):
    talaba = {
'isim': isim,
'familiya': familiya,
}
    talaba.update(qolgan_malumotlar)

    return talaba

talaba1 = talaba_malumotlari("Zilola", "Iskandarova", yosh=15, y_fani="Algebra", sinf=9)
talaba2 = talaba_malumotlari("Shaydo", "Bekturdiyeva", yosh=15, y_fani="Ingliz tili", sinf=9)

print(talaba1)
print(talaba2)


import math

x = 400
print(math.sqrt(x))

print(pow(3,5))



from math import pi
print(pi)



import math

print(math.log2(8))
print(math.log10(100))



import random as r

ismlar = ['olim', 'shuhrat', 'hasan', 'husan', 'anvar']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))




import random as r

x = list(range(0,51,5))
print(x)
print(r.choice(x))




import random as r

x = list(range(11))
print(x)
r.shuffle(x)
print(x)


import math
uzunlik = lambda pi, r: 2*pi*r
print(uzunlik(math.pi,10))


product = lambda x, y : x **y
print(product(3, 2))
def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")



from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))

print(ildizlar)



sonlar = list(range(11))
def daraja2(x):

    return x*x

print(list(map(daraja2, sonlar)))


sonlar = list(range(11))

kvadratlar = list(map(lambda x*xx, sonlar))
print(kvadratlar)