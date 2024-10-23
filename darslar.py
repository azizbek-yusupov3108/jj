# # 1
# def kopaytma(*sonlar):
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija
#
# print(kopaytma(1, 2, 3, 4))
# print(kopaytma(5, 6))
# print(kopaytma(7))
# #
# # 2
# def kvadratlar(son1, son2, son3, *qolgan_sonlar):
#     kvadratlar_royhati = [son1**2, son2**2, son3**2]
#
#     for son in qolgan_sonlar:
#         kvadratlar_royhati.append(son**2)
#
#     return kvadratlar_royhati
#
#
# result = kvadratlar(9, 3, 3, 4, 5, 6)
# print(result)
#
# # 3
# def talaba_malumotlari(isim, familiya, **qolgan_malumotlar):
#     talaba = {
# 'isim': isim,
# 'familiya': familiya,
# }
#     talaba.update(qolgan_malumotlar)
#
#     return talaba
#
# talaba1 = talaba_malumotlari("Zilola", "Iskandarova", yosh=15, y_fani="Algebra", sinf=9)
# talaba2 = talaba_malumotlari("Shaydo", "Bekturdiyeva", yosh=15, y_fani="Ingliz tili", sinf=9)
#
# print(talaba1)
# print(talaba2)






# def tugilgan_yil_hisobla(h_yil=2024):
#     ismi = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     print(f"{ismi}, siz {h_yil-yosh}- yilda tug'ilgansiz")
#
# tugilgan_yil_hisobla()
#
#
# def sonni_hisobla():
#     son = int(input("Sonni kiriting: "))
#
#     kvadrat = son ** 2
#     kub = son ** 3
#
#     print(f"{son} ning kvadrati: {kvadrat}")
#     print(f"{son} ning kubi: {kub}")
#
# sonni_hisobla()
#
#
# def j_yoki_t():
#     son = int(input("Sonni kiriting: "))
#
#     if son % 2 == 0:
#         print(f"{son} soni juft son.")
#     else:
#         print(f"{son} soni toq son.")
#
# j_yoki_t()
#
#
#
# def kattason():
#     son1 = int(input("Birinchi sonni kiriting: "))
#     son2 = int(input("Ikkinchi sonni kiriting: "))
#
#     if son1 > son2:
#         print(f"Katta son: {son1}")
#     elif son1 < son2:
#         print(f"Katta son: {son2}")
#     else:
#         print("Sonlar teng.")
#
# kattason()







# print('sevimli kitobllaringiz')
# savol = 'sevimli kitobingizni kiriting'
# savol+="(dasturni toxtatish uchun 'stop' deb yozing)"
# qiymat=""
# while qiymat !='stop':
#     qiymat = input(savol)
#     print(qiymat)
#
#
#
# while True:
#     yosh = input("Iltimos, yoshingizni kiriting (yoki 'exit' / 'quit' deb yozing): ")
#
#     if yosh.lower() in ['exit', 'quit']:
#         print("Dastur to'xtatildi.")
#         break
#
#     try:
#         yosh = int(yosh)
#
#         if yosh < 7:
#             chipta_narhi = 2000
#         elif 7 <= yosh < 18:
#             chipta_narhi = 3000
#         elif 18 <= yosh < 65:
#             chipta_narhi = 10000
#         else:
#             chipta_narhi = 0
#
#         print(f"Sizning chipta narhingiz: {chipta_narhi} so'm")
#
#     except ValueError:
#         print("Iltimos, to'g'ri yosh kiriting.")
#
#
#
# buyurtma = []
#
# while True:
#     mahsulot = input("mahsulot kiriting (toxtatiw uchun 'stop' deb yozing): ")
#
#     if mahsulot.lower() == 'stop':
#         break
#
#     buyurtma.append(mahsulot)
#     print(f"'{mahsulot}' mahsuloti buyurtma ro'yxatiga qo'shildi.")
#
# print("\nBuyurtma ro'yxati:")
# for i in buyurtma:
#     print(f"- {i}")
#
#
#
#
#
# mahsulotlar = {}
#
# while True:
#     mahsulot = input("Mahsulot nomini kiriting (toxtatiw uchun 'stop' deb yozing): ")
#
#     if mahsulot.lower() == 'stop':
#         break
#
#     narh = input(f"{mahsulot} narhini kiriting: ")
#
#     mahsulotlar[mahsulot] = narh
#
# print("\nSiz kiritgan mahsulotlar va narhlari:")
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot}: {narh}")
