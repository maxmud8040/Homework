# # class Shaxs:
# #     """Shaxslar haqida ma'lumot """
# #     def init(self, ism, familiya, passport, tyil):
# #         self.ism = ism
# #         self.familiya = familiya
# #         self.passport = passport
# #         self.tyil = tyil
# #
# #     def get_info(self):
# #         """Shaxs haqida ma'lumot"""
# #         info = f"{self.ism} {self.familiya}. "
# #         info+=f"Passport: {self.passport}, {self.tyil}-da tug'ilgan. "
# #         return info
# #     def get_age(self, yil):
# #         """Shaxsning yoshini qaytaruvchi metod"""
# #         return yil-self.tyil
# #
# # class Talaba(Shaxs):
# #     def __init__(self,ism,familiya,passport,tyil):
# #         super().__init__(ism,familiya,passport,tyil)
# #
# # talaba = Talaba("Valijon","Aliyev","FA11223344",2000)
# # print(talaba.get_info())
#
# # class Shaxs:
# #     """Shaxslar haqida ma'lumot"""
# #     def __init__(self, ism, familiya, passport, tyil):
# #         self.ism = ism
# #         self.familiya = familiya
# #         self.passport = passport
# #         self.tyil = tyil
# #
# #     def get_info(self):
# #         """Shaxs haqida ma'lumot"""
# #         info = f"{self.ism} {self.familiya}. "
# #         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
# #         return info
# #
# #     def get_age(self, yil):
# #         """Shaxsning yoshini qaytaruvchi metod"""
# #         return yil - self.tyil
# #
# # class Talaba(Shaxs):
# #     """Talaba klassi"""
# #     def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
# #         """Talabaning xususiyatlari"""
# #         super().__init__(ism, familiya, passport, tyil)
# #         self.idraqam = idraqam
# #         self.bosqich = 1
# #         self.manzil = manzil
# #     def get_id(self):
# #         return self.idraqam
# #
# #     def get_bosqich(self):
# #         return self.bosqich
# #
# #     def get_info1(self):
# #         info = f"{self.ism} {self.familiya}. "
# #         info += f"{self.get_bosqich()}-boshqich. ID raqami: {self.idraqam}"
# #         return info
# #
# # class Manzil:
# #     def __init__(self,uy,kocha,tuman,viloyat):
# #         self.uy = uy
# #         self.kocha = kocha
# #         self.tuman = tuman
# #         self.viloyat = viloyat
# #
# #     def get_manzil(self):
# #         manzil = f"{self.viloyat} viloyat ,{self.tuman}-tuman"
# #         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
# #         return manzil
# # talaba_manzil = Manzil(12,"Olmazor","Bog'bon","Samarqand")
# # talaba = Talaba("Valijon","Aliyev","FA112299",2000,"000000012",talaba_manzil)
# #
# # print(talaba.manzil.get_manzil())
#
# #                                                       Uy ishi
# #                                                       1 - topshiriq
# # Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
# #
# # Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# #
# # Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# #
# # Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
# #
# # Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
# #
# # Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# #
# # Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
# #
# # Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
# #
# # Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.
#
# 1-misol
class Talaba:
    def __init__(self,ism,familiya):
        self.ism=ism
        self.familiya=familiya
        self.fanlar=[]

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)


    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz.")

    def fanlarni_korsat(self):
        return self.fanlar


class Fan:
    def __init__(self,fan):
        self.nomi=fan


fan1=Fan("Matematika")
fan2=Fan("Fizika")
fan3=Fan("Tarix")

student=Talaba("Ali","eshmatov")

student.fanga_yozil(fan1)
student.fanga_yozil(fan2)
student.fanga_yozil(fan3)

print(student.fanlarni_korsat())
student.remove_fan("ona tili")
print(student.fanlarni_korsat())



# 2-misol

class Shaxs:
    def __init__(self, ism, yosh):
        self.ism=ism
        self.yosh=yosh

    def get_info(self):
        return f"Ism:{self.ism}, Yosh: {self.yosh}"



class Professor(Shaxs):
    def __init__(self, ism, yosh, fakultet):
        super().__init__(ism, yosh)
        self.fakultet = fakultet

    def get_info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Fakultet: {self.fakultet}"
professor=Professor("Temurbek","18","Matematika")
print(professor.get_info())
print()


class Foydalanuvchi(Shaxs):
    def __init__(self,ism,yosh,email):
        super().__init__(ism,yosh)
        self.email=email
    def get_info(self):
        return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email}"
foydalanuvchi=Foydalanuvchi("hasan","13","hasan21@gmail.com")
print(foydalanuvchi.get_info())
print()



class Admin(Foydalanuvchi):
    def __init__(self,ism,yosh,email,admin):
        super().__init__(ism,yosh,email)
        self.admin=admin

    def get_info(self):
        return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email},Admin:{self.admin}"

    def ban_user(self):
        print("Foydalanuvchi bloklandi")
admin=Admin("husan","32","husan11@gmail.com","admin")
print(admin.get_info())

admin.ban_user()
