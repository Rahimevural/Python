# 1- girilen iki sayıdan hangisi büyüktür
# sayı1 = input("sayı1 gir: ")
# sayı2 = input("sayı2 gir: ")
# result = sayı1 > sayı2
# print(result)

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')


# 2- kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız
#    eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırı

# vize1 = float(input('1.vize: '))
# vize2 = float(input('2.vize: '))
# final= float(input('final: '))

# ortalama = (((vize1 + vize2)/2) * 0.6)+ (final * 0.4)

# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')

      
# 3- girilen bir sayının tek mi çift mi oldduğunu yazdırın 

# sayi = int(input('sayı: '))

# tekcift = (sayi % 2 == 0)
# print(f'girilen sayı çift olma durumu {tekcift}')


# 4- girilen bir sayının negatif pozitif durumunu yazdırın 

# sayi = int(input ('sayı: '))
# negatifpozitif = (sayi >=0 )
# print(f' girilen sayı pozitif olma durumu {negatifpozitif}')



# 5- parola ve email bilgisisni isteyip doğruluğunu kontrol ediniz
#    (email: email@sadikturan.com   parola:abc123)

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email. ')
girilenPassword = input('parola:')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğrumu: {isEmail} ve parola doğru mu:{isPassword}')