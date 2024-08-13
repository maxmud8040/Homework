# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu Alaykum")
#
# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib , unga salom beruvchi funksiya"""
#     print(f"Assalomu Alaykum , Hurmatli {ism.title()}!")
#
# salom_ber('hasan')
#
# print(salom_ber.__doc__)

# def toliq_ism(ism , familiya):
#     """Foydalanuvchi ismini qabul qilib , unga salom beruvchi funksiya"""
#     print(f"Foydalanuvchi ismi : {ism.title()}")
#     print(f"Foydalanuvchi familiyasi : {familiya.title()}")
#
# toliq_ism("Maxmudjon","Shanazarov")

# def yosh_hisobla(tugilgan_yil , joriy_yil = 2024):
#     """Foydslsnuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#
# yosh_hisobla(2008)
# yosh_hisobla(2008,2015)

# def toliq_ism_yasa(ism , familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatirini ishlatamiz
#
# print(toliq_ism_yasa("Maxmudjon" , "Shanazarov"))

# def toliq_ism_yasa(ism , familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatirini ishlatamiz
# talaba1 = toliq_ism_yasa("Seyman","Rajabov")
# talaba2 = toliq_ism_yasa("Usmon","Rahimov")
# print(talaba1)
# print(talaba2)

#
# def toliq_ism_yasa(ism , familiya , otasining_ismi=""):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# print(toliq_ism_yasa("Seyman" , "Rajabov"))


# def avto_info(kompaniya , model , rangi , karobka , yili , narh=None):
#     avto = {
#         "kompaniya":kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "karobka": karobka,
#         "yili": yili,
#         "narh":narh
#     }
#     return avto
# avto1 = avto_info("GM","Cobolt","Oq","Avtamat",2023,13000)
# avto2 = avto_info("Tayota","Supra","Qora","Mehanik",2010 , 30000)
# avtolar = [avto1,avto2]
# print("Online bozordagi mavjud avtomashinalar : ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi'] {avto['model']}. Narhi: {narh}$")
# print(avto1)

# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yhat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1,10))
#                                       Uy ishi
#                                       1 topshiriq
# def yosh_hisobla(ism , tugilgan_yil , joriy_yil = 2024):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz ")
#
# ism = input("Ismingizni kiriting : ")
# yosh = int(input("Yoshingiz nechida : "))
# yosh_hisobla(ism , yosh)
#                                       2 topshiriq
# def hisoblash(son1):
#     print(f"{son1 ** 2} kvadrati : {son1 ** 3} kubi  ")
#
# son = int(input("Son kiriting : "))
# hisoblash(son)
#                                       3 topshiriq
# def juft_yoki_toq(son):
#     if son % 2 == 0:
#         print(f"{son} juft")
#     else:
#         print(f"{son} toq")
# son = int(input("Son kiriting : "))
# juft_yoki_toq(son)
#                                       4 topshiriq
# def katta_yoki_kichik(son1 , son2):
#     if son1 > son2:
#         print(f"{son1} katta {son2} dan")
#     elif son1 < son2:
#         print(f"{son2} katta {son1} dan")
#     else:
#         print("Ikkalasi teng")
# son1 = int(input("1-sonni kiriting : "))
# son2 = int(input("2-sonni kiriting : "))
# katta_yoki_kichik(son1,son2)
#                                       5 topshiriq
# def daraja(x , y):
#     print(f"{x} ning {y} darajasi {x ** y} bo'ladi ")
#     pass
# x = int(input("Xni kiriting : "))
# y = int(input("Yni kiriting : "))
# daraja(x,y)
#                                       6 topshiriq
# def bolish(son):
#     for i in range(2,11):
#         if son % i == 0 :
#             print(f"{son} {i} ga qoldiqsiz bo'linadi.")
#         else:
#             print(f"{son} {i} ga qoldiqli bo'linmaydi.")
#
# son = int(input("Son kiriting : "))
# bolish(son)