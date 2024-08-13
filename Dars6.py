# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu' ,
#         'rang':None ,
#         'yil':'2020' ,
#         'narh':None ,
#         'km':0 ,
#         'karopka':'avto' ,
#         }
#     malibus.append(new_car)
#
#     for malibu in malibus[:3]:
#         malibu['rang'] = 'qizil'
#
#     for malibu in malibus[3:6]:
#         malibu['rang'] = 'qora'
#
#     for malibu in malibus[6:]:
#         malibu['rang'] = 'qora'
#         malibu['karopka'] = 'mexanik'
#
#     for malibu in malibus:
#         if malibu['karopka'] == 'avto':
#             malibu['narh']=40000
#         else:
#             malibu['narh']=35000
#
# print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali': ['html', 'css', 'js'],
#     'hasan': ['php', 'sql'],
#     'husan': ['python', 'php'],
#     'maryam': ['c++', 'c#'],
# }
#
# for ism , tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# hamkasblar = {
#     'ali':{
#         'familiya':'valiyev' ,
#         'tyil':1995 ,
#         'malumot':'oliy' ,
#         'tillar':['python','c++']
#         },
#     'vali':{
#         'familiya': 'aliyev',
#         'tyil':2001 ,
#         'malumot': 'orta maxsus',
#         'tillar': ['html', 'css','js']
#         },
#     'hasan':{
#         'familiya': 'husanov',
#         'tyil':1999 ,
#         'malumot': 'maxsus',
#         'tillar': ['python', 'php']
#         },
#     }
#
# for ism , info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['tyil']}-yilda tug'ilgan , "
#           f"Ma'lumoti: {info['malumot']} , \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper() ,)


#                                       Uy ishi
# 1 topshiriq
# odamlar = {
#     "Abdulloh" : {
#         "ismi" : "Abu Abdulloh Muhammad ibn Ismoil" ,
#         "yoshi" : 810 ,
#         "tugilgan joyi" : "Buxoroda " ,
#         "umr" : 60 ,
#     } ,
#     "Qodiriy" : {
#         "ismi" : "Abdulla Qodiriy" ,
#         "yoshi" : 1894 ,
#         "tugilgan joyi" : "Toshkent" ,
#         "umr" : 44 ,
#     } ,
#     "Erkin" : {
#         "ismi" : "Erkin Vohidov" ,
#         "yoshi" : 1936 ,
#         "tugilgan joyi" : "Farg'ona" ,
#         "umr" : 80 ,
#     } ,
#     "Alisher" : {
#         "ismi" : "Alisher Navoiy" ,
#         "yoshi" : 1441 ,
#         "tugilgan joyi" : "Xirot" ,
#         "umr" : 60 ,
#     } ,
# }
# for ism , info in odamlar.items():
#     print(f"{info['ismi']} . {info['yoshi']}yil {info['tugilgan joyi']}da tug'ilgan . {info['umr']} yil umr ko'rgan ")
# 2 - topshiriq
# odamlar = {
#     "Abu Abdulloh Muhammad ibn Ismoil": ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"],
#     "Abdulla Qodiriy": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
#     "Erkin Vohidov": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziqvuchan Matmusa"],
#     "Alisher Navoiy": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"]
# }
#
# for odam , asar in odamlar.items():
#     print(f"{odam} ning mashhur asarlari:")
#     for work in asar:
#         print(f"- {work}")
#     print()
# 3 - topshiriq
# Odalmar = {
#     "Ali": ["Terminator", "Rambo", "Titanic"],
#     "Vali": ["Tenet", "Inception", "Interstellar"],
#     "Hasan": ["Abdullajon", "Bomba", "Shaytanat"],
#     "Husan": ["Mahallada duv-duv gap", "John Wick"]
# }
#
# for odamlar, kinolar in Odalmar.items():
#     print(f"{odamlar}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(f"{kino}")
#     print()
# 4 - topshiriq
# davlatlar = {
#     "O'zbekiston":{
#         "poytaxt":"Toshkent" ,
#         "hududi":448978 ,
#         "aholisi":33000000 ,
#         "pul birligi":"So'm"
#     } ,
#     "Rassiya":{
#         "poytaxt":"Moskva" ,
#         "hududi":17098246 ,
#         "aholisi":144000000 ,
#         "pul birligi":"Rubl"
#     } ,
#     "AQSH":{
#         "poytaxt":"Washington D.C." ,
#         "hududi":9631418 ,
#         "aholisi":327000000 ,
#         "pul birligi":"Dollar"
#     } ,
#     "Malaysiya":{
#         "poytaxt":"Kuala-Lumpur" ,
#         "hududi":329750 ,
#         "aholisi":250000000 ,
#         "pul birligi":"rinngit"
#     } ,
# }
#
# for davlat , info in davlatlar.items():
#     print(f"\n{davlat}ning poytaxti {info['poytaxt']}"
#           f"\nHududi : {info['hududi']} kv.km"
#           f"\nAholisi : {info['aholisi']}"
#           f"\nPul birligi : {info['pul birligi']}")