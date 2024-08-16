# x = 10
# print(type(x))
#
# matn = "salom"
# print(type(matn))
#
# def salom_ber():
#     print("Assalomu Alaykum")
# print(type(salom_ber))

# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya} , {self.tyil} yilda tug'ilganman")
#
#     def get_name(self):
#         return self.ism
#
#     def get_lastname(self):
#         return self.familiya
#
#     def get_fullname(self):
#         return f"{self.ism} {self.familiya} "
#
#     def get_age(self,yil):
#         return yil - self.tyil
# #
# #
# talaba1 = Talaba("Usmon","Seymanov",2008)
# print(talaba1.get_age(2024))
# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2003)
# talaba4 = Talaba("Hasan","Husanov",2018)

# talaba3.tanishtir()
# print(talaba1.get_fullname() , talaba4.get_fullname())
#
# print(talaba1.ism)
# print(talaba1.familiya)
# print(talaba1.tyil)

#                                                   Uy ishi
#                                                   1 - topshiriq
# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
# class User:
#     def __init__(self,ism,familiya,tyil,qayerda_yashashi,millati):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.qayerda_yashashi = qayerda_yashashi
#         self.millati = millati
#
#     def tanishtirish(self):
#         print(f"Men {self.familiya} {self.ism} , {self.tyil} yilda {self.qayerda_yashashi} tug'ilganman , mening millatim {self.millati}")
#
#
# user1 = User("Maxmud","Shanazarov","2008","Urganch shahri" , "Uzbek")
# user1.tanishtirish()
#
#                                                  2 - topshiriq
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
# class User:
#     def __init__(self,ism , familiya,nick,email):
#         self.ism = ism
#         self.familiya = familiya
#         self.nick = nick
#         self.email = email
#     def get_email(self):
#         return self.email
#     def get_ism(self):
#         return f"{self.ism}"
#     def get_familiya(self):
#         return f"{self.familiya}"
#     def get_info(self):
#         # ism_familiya = self.get_ism_familiya()
#         return (f"Foydalanuvchi {self.nick},\n"
#                 f"Ismi {self.get_ism()},\n"
#                 f"Familiya {self.get_familiya()},\n"
#                 f"Email {self.email}.")
# user1 = User("Maxmud","Shanazarov","Maxmud_8040","maxmud8040@gmail.com")
# print(user1.get_info())
#                                                    3 - topshiriq
# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
# class Users:
#     def __init__(self,ism,familiya,tyil,qayerda_yashashi,millati):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.qayerda_yashashi = qayerda_yashashi
#         self.millati = millati
#
#     def tanishtirish(self):
#         print(f"{self.ism.title()} {self.familiya.title()} ."
#               f"{self.tyil} yilda {self.qayerda_yashashi.title()}da yashaydi ."
#               f"{self.millati.title()} millat vakili .")
#
# user1 = Users("Maxmud","Shanazarov",2008,"Urganch shahar","Uzbek")
# user2 = Users("Usmon","Rahimov",2008,"Sputnik","Uzbek")
# user3 = Users("Seyman","Rajabov",2008,"Xonqa","Bilmiman")
# user4 = Users("Abuser","Abuserov",2000,"Toshkent shahar","Xuyyo")
#
# user1.tanishtirish()
# user2.tanishtirish()
# user3.tanishtirish()
# user4.tanishtirish()