# 1- kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol et. ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.

# name = input('adınız: ')
# age = int(input('yaşınızı giriniz: '))
# eğitim = input('eğitim durumunuzu giriniz: ')

# if (age >= 18):
#      if (eğitim == 'lise' or eğitim=='üniversite'):
#         print(f'{name} ehliyet alabilirsin: ')
#      else:
#           print(f'{name} ehliyet alamazsın eğitim durumun yetersiz: ')    
# else:
#     print(f'{name} ehliyet alamazsın yaşın tutmuyor: ')    



# 2- bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisisni yazdırınız.
#    0-24 = 0
#    25-44 = 1
#    45-54 = 2
#    55-69 = 3
#    70-84 = 4
#    85-100 = 5

# yazili1 = float(input('yazılı1 gir: '))
# yazili2 = float(input('yazılı2 gir: '))
# sözlü = float(input('sözlü gir: '))

# ortalama = (yazili1+yazili2+sözlü)/3

# if (ortalama >= 0 ) and (ortalama < 25 ):
#     print(f'ortalamanız: {ortalama} notunuz: 0')
# elif (ortalama >= 25 ) and (ortalama < 45 ):
#     print(f'ortalamanız: {ortalama} notunuz: 1')
# elif (ortalama >= 45 ) and (ortalama < 55 ):
#     print(f'ortalamanız: {ortalama} notunuz: 2')
# elif (ortalama >= 55 ) and (ortalama < 70 ):
#     print(f'ortalamanız: {ortalama} notunuz: 3')
# elif (ortalama >= 70 ) and (ortalama < 85 ):
#     print(f'ortalamanız: {ortalama} notunuz: 4')
# elif (ortalama >= 85 ) and (ortalama < 100 ):
#     print(f'ortalamanız: {ortalama} notunuz: 5')
# else:
#     print('yanlış bilgi girdiniz. ')


# kendi yaptığım 
# if (ortalama >= 0) and (ortalama <= 24):
#      print('notunuz 0: ')
#      if (ortalama >= 25) and (ortalama <= 44):
#          print('notunuz 1: ')
#          if (ortalama >= 45) and (ortalama <= 54):
#              print('notunuz 2: ')
#              if (ortalama >= 55) and (ortalama <= 69):
#                 print('notunuz 3: ')
#                 if (ortalama >= 70) and (ortalama <= 84):
#                      print('notunuz 4: ')
# else:
#      print('notunuz 5: ')
             


# 3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. bakım = 1. yıl
#    2. bakım = 2. yıl
#    3. bakım = 3. yıl
#    ** süre hesabını alınan gün , ay , yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor. 
#    (simdi) - (2018/8/1) => gün

# import datetime

# tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
# tarih = tarih.split('/')
# trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days <= 365:
#     print('1. servis aralığı')
# elif days > 365 and days <= 365*2:
#     print('2.servis aralığı')
# elif days > 365*2 and days <= 365*3:
#     print('3. servis aralığı')
# else:
#     print('hatalı süre.')








# * girilen bir sayının o-100 arasında olup olmadığını kontrol edin.

# sayi = float(input('bir sayı girin: '))

# if sayi > 0 and sayi <= 100:
#     print(f'sayı: {sayi} , sayı 0-100 aralığında ')
# else:
#     print('sayı 0-100 aralığında değil')


# ** girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# sayi = int(input('bir sayı giriniz: '))

# if sayi >= 0 and sayi % 2 == 0 :
#     print(f'girilrn sayı: {sayi} sayı pozitif çift sayıdır.')
# else:
#     print(f'sayısayi = float(input('bir sayı girin: '))

# if sayi > 0 and sayi <= 100:
#     print(f'sayı: {sayi} , sayı 0-100 aralığında ')
# else:
#     print('sayı 0-100 aralığında değil')')


# sayi = int(input('sayı: '))

# if (sayi > 0):
#     if (sayi % 2 == 0):
#         print('girilen sayı pozitif çift sayıdır.')
#     else:
#         print('girilen sayı pozitif ancak tek.')
# else:
#     print('girilen sayı negatif sayı.')


# *** email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input('email gir: ')
# girilenPassword = input('password gir: ')

# if girilenEmail == email :
#     if girilenPassword == password:
#         print('giriş başarılı.')
#     else:
#         print('parolanız yanlış.')
# else:
#     print('email yanlış')    




# Girilen üç sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a > b and a > c :
#     if b > a and b > c :
#         if c > a and c > b:
#             print('a en büyük sayıdır.')
#     else:
#         print('b en büyük sayıdır.')
# else:
#      print('c en büyük sayıdır.')
       

# Kullanıcıdan 2 vize (%60) ve final(%40) notu alıp ortalama hesaplayınız.
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a- ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b- finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('vize1: '))
# vize2 = float(input('vize2: '))
# final = float(input('final: '))
# ortalama = ((vize1+vize2)/2)*0.6 + (final*0.4)

# if ortalama >= 50 :
#     print(f'öğrencinin ortalaması:{ortalama} ve gecme durumu : başarılı')
# else:
#     if (final >= 70):
#         print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: başarılı.')
#     else:
#         print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: başarısız')
  


# 6- kişinin ad ,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    formül: (kilo/boy uzunluğunun karesi)
#    aşağıdaki tabloya göre kişi hangi gruba girmektedir
#    0-18.4 => zayıf
#    18.5-24.9 => normal
#    25.0-29.9 => fazla kilolu
#    30.0-34.9 => şişman




name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))
index = (kg) /( hg**2)


zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
fazlakilolu = (index >= 25.0) and (index <= 29.9)
obez = (index >= 30.0) and (index <= 34.9)



if (index >= 0) and (index <= 18.4):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen : zayıf')
elif (index >= 18.5) and (index <= 24.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen : normal')
elif (index >= 25.0) and (index <= 29.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen : fazlakilolu')
elif (index >= 30.0) and (index <= 34.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen : obez')
else:
    print('bilgileriniz yanlış.')


# print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
# print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
# print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen fazlakilolu: {fazlakilolu}')
# print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')