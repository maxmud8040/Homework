# import math
# uzunlik = lambda pi , r : 2*pi*r
# print(uzunlik(math.pi , 10))

# product = lambda x , y : x ** y
# print(product(5,10))

# def daraja (n):
#     return lambda x : x ** n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga , kub {kub(3)} ga teng")

# from math import sqrt
#
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# sonlar = list(range(11))

# def daraja2(x):
#     return x*x
# print(list(map(daraja2,sonlar)))

# sonlar = list(range(11))
# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

# sonlar = list(range(11))
# a = [3 , 4 , 5]
# b = [7 , 8 , 9]
# a_plus_b = list(map(lambda x,y : x+y , a , b))
# print(a_plus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn : matn.upper(),ismlar))

# import random
# sonlar = random.sample(range(100),10)
#
# def juft(x):
#     return x % 2 == 0
#
# juft_sonlar = list(filter(juft,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random
# sonlar = random.sample(range(100),10)

# juft_sonlar = list(filter(lambda son : son % 2 == 0 , sonlar))
# print(sonlar)
# print(juft_sonlar)

# mevalar = ['olma','anor','anjir','shaftoli',"o'rik",'tarvuz','qovun','banan']
#
# mevalar_b = list(filter(lambda meva : meva.startswith('a'),mevalar))
# print(mevalar_b)
#
# mevalar2 = list(filter(lambda meva : len(meva)<5,mevalar))
# print(mevalar2)

# 1-masala: Sonlarni ko'paytirish
# Vazifa: Berilgan sonlar ro'yxatidagi barcha sonlarni o'zaro ko'paytirib, yakuniy natijani qaytaruvchi funksiyani lambda yordamida yozing.

# Ishlab bilmadim !!!

# 2-masala: So'zlar uzunligini aniqlash
# Vazifa: Berilgan so'zlar ro'yxatidagi har bir so'zning uzunligini aniqlab, (so'z, uzunlik) shaklidagi tuplamlar ro'yxatini hosil qiling.

# soz = ['olma','anor','anjir','shaftoli',"o'rik",'tarvuz','qovun','banan']
#
# soz_uzunlik = list(filter(lambda meva : len(meva)<5,soz))
# soz_
# print(mevalar2)

# 3-masala: Musbat sonlarni ajratib olish
# Vazifa: Berilgan sonlar ro'yxatidan faqat musbat sonlarni ajratib oluvchi lambda funksiyasini yozing.