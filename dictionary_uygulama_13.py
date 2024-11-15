'''
   ogrenciler = {
       '120':{
            'ad': 'Ali',
            'soyad': 'yılmaz',
            'telefon': '532 000 00 01'
       } , 



    ogrenciler = {
       '125':{
            'ad': 'can',
            'soyad': 'korkmaz',
            'telefon': '532 000 00 02'
       },

    ogrenciler = {
       '128':{
            'ad': 'volkan',
            'soyad': 'yükselen',
            'telefon': '532 000 00 03'
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
    dictionary içinde saklayınız


    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
'''

öğrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# öğrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }

#update metodu ile :

öğrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

print(öğrenciler)
öğrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

öğrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

print(öğrenciler)
öğrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

öğrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
print(öğrenciler)

ogrNo = input('öğrenci no')
öğrenci = öğrenciler[number]

print(öğrenci)
                    