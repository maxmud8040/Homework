# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
#
# print(oraliq(0,10))
# print(oraliq(10,21))

# def avto_info(kompaniya , model , rang , karopka , yili , narh = None):
#     avto = {
#         "komparniya":kompaniya ,
#         "model": model,
#         "rang": rang,
#         "karopka": karopka,
#         "yili": yili,
#         "narh": narh,
#     }
#     return avto
#
# print("Saytimizdagi avtolar ro'yhatini shakillashtiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting : " , end='')
#     kompaniya = input("Ishlab chiqaruvchi : ")
#     model = input("Model : ")
#     rang = input("Rangi : ")
#     karopka = input("Karopka : ")
#     yili = input("Yili : ")
#     narh = input("Narh : ")
#
#     avtolar.append(avto_info(kompaniya,model,rang,karopka,yili,narh))
#
#     javob = input("Yana avto qo'shasizmi? (yes/no)")
#     if javob == 'no':
#         break
# print("\n",avtolar)

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting : ")
#         baholar[ism] = baho
#     return baholar
#
# talabalar = ['Seyman','Bobur','Usmon','Sarvar',]
# baholar = bahola(talabalar)
# print(baholar)

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#
# ismlar = ['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2,3,4,5,6,7,8,9))

# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(1,2,6,6,5,89,4,9,))

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
#
# print(summa(5,6,8,9,7))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar
#
# avto1 = avto_info("GM","Maluba",rangi = "qora" , yili = 2020)
# avto2 = avto_info("Kia","K5",rangi = "qizil" , narh = 35000)
#
# print(avto1,avto2)
#                                   Uy ishi
#                                   1 topshiriq
# def sonlar(*sonlar):
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija
# print(sonlar(2, 3, 4))
#                                   2 topshiriq
# def talaba_malumotlari(ism, familiya, **qoshimcha_malumotlar):
#     talaba = {
#         'Ism': ism,
#         'Familiya': familiya
#     }
#     talaba.update(qoshimcha_malumotlar)
#     return talaba
# talaba1 = talaba_malumotlari('Ali', 'Valiyev', yosh=20, kurs=2, fakultet='Informatika')
# talaba2 = talaba_malumotlari('Zarina', 'Ahmedova', yosh=21, kurs=3)
#
# print(talaba1)
# print(talaba2)