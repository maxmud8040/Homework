# with open("File.txt") as fayl:
#     pi = fayl.read()
# print(Hey)
# fayl = open('File.txt')
# pi = fayl.read()
# print(pi)
# fayl.close()

# pi = pi.rstrip()
# pi = pi.replace("\n"," ")
# pi = float(pi)
# print(pi)
# print(type(pi))

# filename = "Talabalar.txt"
# with open(filename) as file:
#     talabalar = file.readlines()
#
#
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# filename2 = 'teachers.txt'
# with open(filename2,'w') as fayl2:
#     fayl2.write("Jonibek")
#
# print(fayl2)

# filename3 = 'new_file.txt'
# ism = "Maxmud Shonazarov "
# tyil = "2008"
# with open(filename3,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(tyil)

# filename3 = 'new_file.txt'
# ism = "Maxmud Shonazarov "
# tyil = 2004
# with open(filename3,'w') as fayl:
#     fayl.write(ism + "\n")
#     fayl.write(str(tyil) + "\n")
# with open(filename3,'a') as file5:
#     file5.write("Seyman Rajabov \n")
#     file5.write("2008")

# import pickle
#
# talaba1 = {"ism":"Maxmud","familiya":"Shonazarov","tyil":2008,"Kurs":0}
# talaba2 = {"ism":"Usmon","familiya":"Rahimov","tyil":2008,"Kurs":0}
#
# with open("info","wb") as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)
#
# with open("info","rb") as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
#
# print(talaba1)
# print(talaba2)

# Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan).
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
#
# Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# tyil = 28042006 #Mani tug'ilgan yilimni kiritib bo'lmadi 07072008
# with open("pi_million_digits.txt") as fayl:
#     pi = fayl.read()
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi_float = float(pi)
# if float(pi) in tyil:
#     print(f"pi file da sizni {tyil} tug'ilgan yil sanangiz bor ekan")
# else:
#     print(f"Sizni {tyil} tug'ilgan yil sanangiz yo'q ekan ekan")

