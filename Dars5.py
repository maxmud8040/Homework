# 1 - topshiriq
# lugat = {
#     'Float':'Onlik son' ,
#     'If':'Shartlarni tekshirish operatori' ,
#     'For':'Biror amalni qayta-qayta bajarish sikli' ,
#     'Integer':'Butun son' ,
#     'Boolean':'Mantiqiy qiymat' ,
# }
# for kalit , qiymat in sorted(lugat.items()):
#     print(f'{kalit.title()} : {qiymat}')


# 2 - topshiriq
# davlatlar = {
#     'AQSH' : 'Washington D.C.' ,
#     'ITALIYA' : 'Rim' ,
#     'MALAYZIYA' : 'Kuala-Lumper',
#     'OZBEKISTON' : 'Toshkent',
#     'QIRGIZISTON' : 'Bishkek' ,
#     'QOZOQISTON' : 'Astana' ,
#     'RASSIYA' : 'Moskva' ,
#     'SINGGAPUR' : 'Sungapur' ,
#     'TOJIKISTON' : 'Dushanbe '
# }
# davlat=[]
# poytaxt=[]
# for d, p in davlatlar.items():
#     davlat.append(d)
#     poytaxt.append(p)
# print(*sorted(davlat))
# print(*sorted(poytaxt))

# 3 - topshiriq
# davlatlar={
#     "AQSH":"Washington D.C",
#     "Malayziya":"Bishkek",
#     "Italiya":"Rim",
#     "O'zbekiston":"Toshkent",
#     "Qirg'iziston":"Dushanbe"
# }
# davlat = str(input('Qaysi davlatni poytaxtini bilishni istaysiz : '))
#
# if davlat in davlatlar:
#     print(f"{davlat} ning poytaxti {davlatlar[davlat]}")
# else:
#     print(f"Kechirasiz bizda {davlat}ni poytaxti yo'q")
