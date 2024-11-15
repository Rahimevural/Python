# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
# x1 = float(input('bir sayı girin: '))
# result = (x1>0) and (x1<100)

# sayi = float(input('sayı: '))

# result = (sayi > 0) and (sayi<=100)
# print(f'sayı 0-100 arasında mı: {result}')


# 2- girilen bir sayının pozitif çift sayı olup olmadıgını kontrol ediniz
# x2 = int(input('bir sayı giriniz: '))
# result = (x2%2==0) and (x2>=0)

# sayi = int(input('sayı: '))
# result = (sayi > 0) and (sayi % 2 == 0)
# print(f'girilen sayı pozitif çift sayı mı: {result}')


# 3- email ve parola bilgileri ile giriş kontrolu yapınız
# email = 'email@sadikturan'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ' )

# result = (girilenEmail == email) and (girilenPassword == password)
# print = (f'uygulamaya giriş başarılı mı: {result}')



# 4- girilen üç sayıyı büyüklük olarak karşılaştırınız

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and (a > c)
# print(f'a en buyuk sayıdır: {result} ')


# result = (b > a) and (b > c)
# print(f'b en buyuk sayıdır: {result} ')


# result = (c > b) and (c > a)
# print(f'c en buyuk sayıdır: {result} ')


# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    eğer ort 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a) ort 50 olsa bile final notu en az 50 olmalıdır
#    b) finalden 70 alındığında ort önemi olmasın

# vize1 = float(input('vize1: '))
# vize2 = float(input('vize2: '))
# final = float(input('final: '))

# ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
# result = (ortalama >=  50) and ( final >= 50)
# result = (ortalama >= 50) or (final >= 70)

# print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')


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



print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen fazlakilolu: {fazlakilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')