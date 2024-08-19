# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya} . {self.bosqich}-bosqich talabasi"
#
#     def set_bosqich(self,bosqich):
#         self.bosqich = bosqich

    # def update_bosqich(self):
#         self.bosqich += 1
# print(talaba1.get_info())
# talaba1 = Talaba("Seyman","Rajabov","2008")
# talaba1.bosqich = 2
# print(talaba1.get_info())
# talaba1.set_bosqich(3)
# talaba1.update_bosqich()
# talaba1.update_bosqich()
# print(talaba1.get_info())

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
#
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Maxmud","Shanazarov",2008)
# talaba2 = Talaba("Seyman","Rajabov",2008)
# talaba3 = Talaba("Usmon","Rahimov",2008)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
#
# print(matematika.talabalar_soni)
# mat_talabalar= matematika.get_students()
# print(mat_talabalar)
#
# print(dir(Talaba))
# print(dir(Fan))
#
# def see_methonds(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]
#
# print(see_methonds(Talaba))
# print(see_methonds(Fan))
# print(see_methonds(talaba1))
# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())



#                                           Uy ishi
#                                           1 - topshiriq
# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

# class Avto:
#     def __init__(self,model, rang,yil, korobka, narh):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.km = 0
#         self.yil = yil
#                                           2 - topshiriq
# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#                                           Malumot !!!
    # def malumot(self):
    #     return (f"Model : {self.model} , Rang : {self.rang} , Yili : {self.yil}\n"
    #             f"Karopka : {self.korobka} , Narhi : {self.narh}so'm \n"
    #             f"{self.km}km yurgan")
# avto1 = Avto("Malibu","Qora",2024,"Avtomat",400000000)
# print(avto1.malumot())


#                                           3 - topshiriq
# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#                                           Ishlanmadi !!!

#                                           4 - topshiriq
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

#     def update_km(self):
#         self.km += 1000
# avto1 = Avto("Malibu", "Qora", 2024, "Avtomat", 400000000)
# avto1.update_km()
# print(avto1.malumot())
#                                           5 - topshiriq
# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

# class AvtoSalon:
#     def __init__(self,salon_nomi,manzili,*sotiladigan_moshinalar):
#         self.salon_nomi = salon_nomi
#         self.manzili = manzili
#         self.sotiladigan_moshinalar = sotiladigan_moshinalar
#         self.avtolar = []
#
#     def add_avto(self,avto):
#         self.avtolar.append(avto)
#     def all_cars(self):
#         for avto in self.avtolar:
#             print(avto.avto_info())
#     def malumot(self):
#         return (f"{self.manzili}da joylashgan {self.salon_nomi} nomli salonda {self.sotiladigan_moshinalar} moshinalar bor")
# avtosalon = AvtoSalon("Avtoolam","Sputnik","Malibu","Spark","Nexia","Matiz")
# print(avtosalon.malumot())

#                                           6 - topshiriq
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# class Avto:
#     def __init__(self,model,rang,yili,koropka,narh,km = 0):
#         self.model = model
#         self.rang = rang
#         self.yili = yili
#         self.koropka = koropka
#         self.narh = narh
#         self.km = km
#     def avto_info(self):
#         return f"{self.yili} yil {self.rang} rangli {self.model} moshina \n Karopka {self.koropka} {self.km}km yurgan , Narhi esa {self.narh}"
#
# avto1 = Avto("Malibu","Qora",2024,"Avtomat",400000000,5000)
# avto2 = Avto("Supra","Oq",1990,"Mexanik",750000000,150000)

avtosalon.add_avto(avto1)
avtosalon.add_avto(avto2)

avtosalon.all_cars()
#                                            7 - topshiriq
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
#
# avtosalon.all_cars()#
#                                             8 - topshiriqh
# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
#                                   Tushunmadim !!!

#                                           9 - topshiriq
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)
# print(dir(Avto))
# print(dir(AvtoSalon))
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]
# print(see_methods(Avto))
# print(see_methods(AvtoSalon))
