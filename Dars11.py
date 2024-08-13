# import avto_info_mod as aim
#
# avto1 = aim.avto_info("GM","Malibu","Qora","avtamat",2018,40000)
# aim.info_print(avto1)
#
# from avto_info_mod import info_print , avto_info
#
# avto1 = avto_info("GM","Malibu","Qora","avtamat",2018,40000)
# info_print(avto1)

# from avto_info_mod import info_print as ip , avto_info as ai
#
# avto1 = ai("GM","Malibu","Qora","avtamat",2018,40000)
# ip(avto1)

# from avto_info_mod import *
#
# avto1 = avto_info("GM","Malibu","Qora","avtamat",2018,40000)
# info_print(avto1)

# import math
# x = 400
# print(math.sqrt(x))

# print(pow(6,8))
# from math import pi
# print(pi)

# import math
# # from math import log2 , log10
# print(math.log2(8))
# print(math.log10(100))

# import random as r
# son = r.randint(0,100)
# print(son)

# import random as r
# ismlar = ["olim","anvar","hasan","husan"]
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# import random as r
#
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# import random as r
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# Masala 1: Kvadrat ildizni topish
# Masala: Sizga x=144 berilgan. math.sqrt funksiyasidan foydalanib, x-ning kvadrat ildizini toping.

# from math import *
# x = 144
# print(sqrt(x))

# Masala 2: Darajaga oshirish
# Masala: Sizga a=2 va b=10 berilgan. math.pow funksiyasidan foydalanib, a ning b-darajasini hisoblang.

# from math import *
# a = 2
# b = 10
# print(pow(a,b))

# Masala 3: Sinus qiymatini topish
# Masala: Sizga burchak a=30 gradus burchak  berilgan. math.sin funksiyasidan foydalanib,a ning sinusini toping. Eslatma: math.sin radianlar bilan ishlaydi, shuning uchun burchakni radianlarga o'girish kerak bo'ladi.

# from math import *
# a = 30
# print(sin(a))

# Masala 4: Tasodifiy son yaratish
# Masala: Sizga 𝑎=55 va b=155 berilgan. random.randint funksiyasidan foydalanib, shu oraliqda tasodifiy butun son yarating.

from random import *
a = 55
b = 155
print(randint(a,b))

# Masala 5: Tasodifiy element tanlash
# Masala: Sizga quyidagi ro'yxat berilgan: colors = ["qizil", "yashil", "ko'k", "sariq", "qora"]. random.choice funksiyasidan foydalanib, ro'yxatdan tasodifiy rangni tanlang.
# from random import *
# colors = ["qizil", "yashil", "ko'k", "sariq", "qora"]
# print(choice(colors))