# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon):
#     malumotlar = {
#         "Ism": ism,
#         "Familiya": familiya,
#         "Tug'ilgan yili": tugilgan_yil,
#         "Tug'ilgan joyi": tugilgan_joy,
#         "Email": email,
#         "Telefon raqami": telefon
#     }
#     return malumotlar
#
# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
# tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
# email = input("Email manzilingizni kiriting: ")
# telefon = input("Telefon raqamingizni kiriting: ")
#
# foydalanuvchi = foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon)
# print(foydalanuvchi)



# 2 ish

# from datetime import datetime
#
#
# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, telefon=None):
#
#
# hozirgi_yil = datetime.now().year
# yosh = hozirgi_yil - tugilgan_yil
#
# malumotlar = {
# "Ism": ism,
# "Familiya": familiya,
# "Tug'ilgan yili": tugilgan_yil,
# "Yoshi": yosh,
# "Tug'ilgan joyi": tugilgan_joy,
# "Email": email if email else "Email manzili kiritilmagan",
# "Telefon raqami": telefon if telefon else "Telefon raqami kiritilmagan"
# }
# return malumotlar
#
# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
#
# # Ixtiyoriy ma'lumotlar
# email = input("Email manzilingizni kiriting (ixtiyoriy): ") or None
# telefon = input("Telefon raqamingizni kiriting (ixtiyoriy): ") or None
#
# foydalanuvchi = foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon)
# print(foydalanuvchi)


#
# 3 ish


# from datetime import datetime
#
#
# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, telefon=None):
#
#
# hozirgi_yil = datetime.now().year
# yosh = hozirgi_yil - tugilgan_yil
#
# malumotlar = {
# "Ism": ism,
# "Familiya": familiya,
# "Tug'ilgan yili": tugilgan_yil,
# "Yoshi": yosh,
# "Tug'ilgan joyi": tugilgan_joy,
# "Email": email if email else "Email manzili kiritilmagan",
# "Telefon raqami": telefon if telefon else "Telefon raqami kiritilmagan"
# }
# return malumotlar
#
# mijozlar = []
#
# while True:
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
#
#     email = input("Email manzilingizni kiriting (ixtiyoriy): ") or None
#     telefon = input("Telefon raqamingizni kiriting (ixtiyoriy): ") or None
#
#     mijoz = foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon)
#     mijozlar.append(mijoz)
#
#     # Yana bir mijoz qo'shishni xohlaysizmi?
#     davom_ettirish = input("Yana bir mijoz qo'shishni xohlaysizmi? (ha/yo'q): ").lower()
#     if davom_ettirish != 'ha':
#         break
#
# print("\nMijozlar ro'yxati:")
# for mijoz in mijozlar:
#     print(mijoz)



# 4 ish

#
# def eng_katta_son(a, b, c):
#     return max(a, b, c)
#
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = float(input("Uchinchi sonni kiriting: "))
#
# eng_katta = eng_katta_son(a, b, c)
# print(f"Eng katta son: {eng_katta}")