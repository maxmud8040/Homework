# from uuid import uuid4
#
# class Avto:
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
#
#     def add_km(self,km):
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashinada km qaytarib bo'lmaydi")
# avto1 = Avto("GM","Cobolt","Oq",2024,35000)
# avto1 = Avto("GM","Nexia","Sori",2008,8000)
# avto1 = Avto("GM","Tahoe","Qora",2024,80000)
# print(Avto.get_num_avto())
#                                             Uy ishi



# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq  xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
#
# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
#
# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing

# class Shaxs:
#
#     def __init__(self, ism, yosh,koder):
#         self.ism=ism
#         self.yosh=yosh
#         self.__koder = koder
#         self.__site += 1
#     def get_info(self):
#         return f"Ism:{self.ism}, Yosh: {self.yosh}"
#
#
#
# class Professor(Shaxs):
#     def __init__(self, ism, yosh, fakultet):
#         super().__init__(ism, yosh)
#         self.fakultet = fakultet
#
#     def get_info(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}, Fakultet: {self.fakultet}"
# professor=Professor("Temurbek","18","Matematika")
# print(professor.get_info())
# print()
#
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self,ism,yosh,email):
#         super().__init__(ism,yosh)
#         self.email=email
#     def get_info(self):
#         return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email}"
# foydalanuvchi=Foydalanuvchi("hasan","13","hasan21@gmail.com")
# print(foydalanuvchi.get_info())
# print()
#
#
#
# class Admin(Foydalanuvchi):
#     def __init__(self,ism,yosh,email,admin):
#         super().__init__(ism,yosh,email)
#         self.admin=admin
#
#     def get_info(self):
#         return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email},Admin:{self.admin}"
#
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi")
# admin=Admin("husan","32","husan11@gmail.com","admin")
# print(admin.get_info())
#
# admin.ban_user()