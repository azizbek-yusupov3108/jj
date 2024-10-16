# 1
def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(1, 2, 3, 4))
print(kopaytma(5, 6))
print(kopaytma(7))
#
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
