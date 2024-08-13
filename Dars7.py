# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son+1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) : "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)


#
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) : "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) : "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 11:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# ismlar = []
# print("Yaqin do'stingizni ro'yhatga kiritamiz")
# n=1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting : "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Do'stlaringizni ro'yhati : ")
# for ism in ismlar:
#     print(ism.title() , end=" ")

# print("Do'stlaringizni yoshini saqlaymiz")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting : ")
#     yosh = input(f"{ism.title()}ning yoshi nechida : ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ma'lumot qo'shasizmi ? (ha/yoq) : ")
#     if javob == "yoq":
#         ishora = False
#
#
# for ism , yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ["lacetti","nexia","toyota","nexia","audi","nexia","malibu"]
# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)

# talabalar = ['jonibek','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting : ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
#
# print(baholangan_talabalar)
#                                               Uy ishi!!!
                                                #1-topshiriq
# kitob = []
# ishora = True
# while ishora:
#     sorov = input("Yaxshi ko'rgan kitobingizni kiriting : ")
#     kitob.append(sorov)
#     sorov2 = input("Yana kitob qo'shasizmi(yes/no)")
#     if sorov2 != 'no':
#         continue
#     else:
#         ishora = False
# print(kitob)
                                                # 2-topshiriq
# ishora = True
# while ishora:
#     sorov = int(input("Nechi yoshsiz : "))
#     sorov = int(sorov)
#
#     if sorov < 7:
#         narx = 2000
#     elif sorov <= 18:
#         narx = 3000
#     elif sorov <= 65:
#         narx = 10000
#     else:
#         narx = 0
#
#
#     print(f"Chiptaning narxi: {narx} so'm")
#
#     sorov2 = input("Yana chipta olasizmi (Dasturni to'xtatish uchun (exit yoki quit) deb yozing : ")
#     if sorov2 in ['exit','quit']:
#         print("Dastur to'xtatildi")
#         ishora = False
                                                #3-topshiriq
# ombor = []
# ishora = True
# while ishora:
#     sorov = input("Mahsulotni nomini kiriting : ")
#     ombor.append(sorov)
#     sorov2 = input("Yana qo'shasizmi(yes/no)")
#     if sorov2 in 'no':
#         print("Dastur to'xtatildi")
#         ishora = False
# print(ombor)
                                                #4-topshiriq

e_bozor = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = float(input(f"{mahsulot} narxini kiriting: "))
    e_bozor[mahsulot] = narx

    yana = input("Yana qo'shasizmi? (ha yoki yo'q): ")
    if yana != 'ha':
        break

print("E-bozordagi mahsulotlar va ularning narxlari:", e_bozor)






















