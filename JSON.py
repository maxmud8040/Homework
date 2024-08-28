import json
#
# x = 10
# x_json = json.dumps(x)
# print(type(x_json))
#
# ism = "Maxmudjon"
# ism_json = json.dumps(ism)
# print(ism_json)
#
# sonlar = [10,15,48,65,32,0]
# sonlar_json = json.dumps(sonlar)
# # print(sonlar_json)
# bemor = {
#     "ism":"Alijon",
#     "yosh":30,
#     "oila":True,
#     "farzandlar":("O'qtam","Toshmat"),
#     "allergiya":None,
#     "dorilar":[
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi": "Panadol", "miqdori": 1.2}
#     ]
# }
#
#
#
# bemor_json = json.dumps(bemor,indent=3)
#
# bemor = json.loads(bemor_json)
# print(type(bemor))
# # print(bemor_json)
# with open("Bemor.json","w") as f:
#     json.dump(bemor,f)
#
# filename = "Bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)
# print(type(bemor))
#
# data = {
#     "address_components": [
#         {
#             "long_name": "Tinchlik Street",
#             "short_name": "Tinchlik Street",
#             "types": [
#                 "political",
#                 "sublocality",
#                 "sublocality_level_1"
#             ]
#         },
#         {
#             "long_name": "Khorezm",
#             "short_name": "Khorezm",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Khorezm Region",
#             "short_name": "Khorezm Region",
#             "types": [
#                 "administrative_area_level_1",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Uzbekistan",
#             "short_name": "UZ",
#             "types": [
#                 "country",
#                 "political"
#             ]
#         }
#     ],
#     "formatted_address": "Tinchlik Street, Khorezm, Urgench",
#     "geometry": {
#         "bounds": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         },
#         "location": {
#             "lat": 41.55860870120288,
#             "lng": 60.6218083747805
#         },
#         "location_type": "APPROXIMATE",
#         "viewport": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         }
#     },
#     "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
#     "types": [
#         "political",
#         "sublocality",
#         "sublocality_level_1"
#     ]
# }
#
# kenglik = data['geometry']['location']['lat']
# uzunlik = data['geometry']['location']['lng']
# print(f"{kenglik},{uzunlik}")

# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
#
# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
#
# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
#
    # Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.

# 1 - topshiriq
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# with open("data.json","w") as f:      # Data ni Json malimotiga o'tkazadi
#     json.dump(data,f)

# 2 - topshiriq
# talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
# with open("talaba.json","w") as f:
#     json.dump(talaba_json,f)
# 3 - topshiriq
# with open("students.json","r") as f:
#     students = json.load(f)
# for student in students["student"]:
#     ism = student["name"]
#     familiya = student["lastname"]
#     kurs = student["year"]
#     fakultet = student["faculty"]
#     print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} fakulteti talabasi")

students = {"student":
    [
        {"id":"01",
        "name": "Tom",
         "lastname": "Price",
         "year": 4,
         "faculty": "Engineering"
         },
        {"id": "02",
         "name": "Nick",
         "lastname": "Thameson",
         "year": 3,
         "faculty": "Computer Science"
        },
        {"id": "03",
         "name": "John",
         "lastname": "Doe",
         "year": 2,
         "faculty": "ICT"}
    ]
}
for student in students["student"]:
    ism = student["name"]
    familiya = student["lastname"]
    kurs = student["year"]
    fakultet = student["faculty"]
    print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} fakulteti talabasi")
