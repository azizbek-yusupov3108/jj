class Avto:
    def __init__(self,model,rang,narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.km = 3

    def get_info(self):
        return f"modeli-{self.model} rangi-{self.rang} narh-{self.narh} {self.km} - km yurgan"
    # def set_km(self.km):
    #     self.km = km
    def update_km(self):
        self.km += 1

avto1 = Avto('nexia 2','oq','10000$')
print(avto1.get_info())
# avto1.set_km(2021)
# print(avto1.get_info())

avto1.update_km()
print(avto1.get_info())

avto1.update_km()
print(avto1.get_info())


class Avtosalon:
    def __init__(self,salon_nomi,manzili,s_avtomobillar):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.s_avtomobilllar = s_avtomobillar




class Avto:
    def __init__(self, model, rang, narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.km = 8

    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Narh: {self.narh}, {self.km} km yurgan"

    def set_km(self, km):

        if km >= self.km:
            self.km = km
        else:
            print("Yangi kilometraj eski kilometrajdan katta bo'lishi kerak.")

    def update_km(self):

        self.km += 1


# class Avtosalon:
#     def __init__(self, salon_nomi, manzil):
#         self.salon_nomi = salon_nomi
#         self.manzil = manzil
#         self.sotuvdagi_avtomobillar = []
#
#     def avtomobil_qoshish(self, avtomobil):
#         self.sotuvdagi_avtomobillar.append(avtomobil)
#
#     def avtomobillarni_korish(self):
#         return [avto.get_info() for avto in self.sotuvdagi_avtomobillar]
#
#     def salon_malumoti(self):
#         return (f"Salon Nomi {self.salon_nomi}, "
#                 f"Manzil {self.manzil}, "
#                 f"Sotuvdagi Avtomobillar {len(self.sotuvdagi_avtomobillar)} ta")
#
#
# avto1 = Avto('nexia 2', 'moviy', '9000$')
# avto2 = Avto('cobalt', 'zeus', '14000$')
#
# salon = Avtosalon("GM", "Khiva")
#
# salon.avtomobil_qoshish(avto1)
# salon.avtomobil_qoshish(avto2)
#
# print(salon.salon_malumoti())
# print(salon.avtomobillarni_korish())
#
#
# avto1.update_km()
# print(avto1.get_info())
#
# avto1.set_km(2021)
# print(avto1.get_info())
