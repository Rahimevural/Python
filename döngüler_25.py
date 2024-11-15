# FOR DÖNGÜSÜ 

# numbers = [1,2,3,4,5]

# for a in numbers:
#     print('hello')

# names = ['ali','ahmet','ayşe']

# for name in names:
#     print(f'benim adım {name}')

# name = 'sadık turan'

# for n in name:
#     print(n)

# tuple = [(1,2),(1,3),(3,5),(5,7)]
# for a,b in tuple:
#     print(a)


# # dictionaryde bu şekilde çalışmaz şu şekilde olur.

# d = {'k1':1,'k2':2,'k3':3}

# for key,value in d.items():
#     print(key)

# sayilar = [1,3,5,7,9,12,19,21]

# 1- sayılar listesindeki hangı sayılar 3 ün katıdır?
# for sayi in sayilar:
#     if (sayi%3 == 0 ):
#         print(sayi)


# 2- sayılar listesinde sayıların toplamı kaçtır?
# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
#     print('toplam: ', toplam)



# 3- sayılar listesindeki tek sayıların karesini alınız.

# for sayi in sayilar:
#     if (sayi % 2 == 1):
#         print(sayi**2)


# sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- sehirlerden hangileri en fazla 5 karakterlidir ? 

# for sehir in sehirler:
#     if (len(sehir) <= 5):
#         print(sehir)

# urunler = [
#     {'name': 'samsung s6','price' : '3000'},
#     {'name': 'samsung s7','price' : '4000'},
#     {'name': 'samsung s8','price' : '5000'},
#     {'name': 'samsung s9','price' : '6000'},
#     {'name': 'samsung s10','price' : '7000'},
# ]

#5- ürünlerin fiyatları toplamı nedir ? 
# toplam = 0
# for urun in urunler:
#     fiyat = int(urun['price'])
#     toplam += fiyat
# print('toplam ürün fiyatı: ', toplam)

# 6- ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

# for urun in urunler:
#     if (int(urun['price']) <= 5000):
#         print(urun['name'])
    



# WHİLE DÖNGÜSÜ

# 1-100 e kadar yazdır

# x = 0
# while x < 100:
#     print(x)
#     x = x + 1
# print('bitti...')

# x = 1
# while x <= 100:
#     if x % 2==1:
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1
# print('bitti...')


# name = ' ' # false
# while not name.strip():
#     name = input('isminizi giriniz: ')

# print(f'merhaba, {name}')
sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın.
# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1
# for i in sayilar:
#     print(i)


    
# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları
#    ekrana yazdırın.

# baslangic = int(input('başlangıç: '))
# bitis = int(input('bitiş: '))

# i = baslangic
# while i < bitis:
#     i += 1 
#     if (i % 2 == 1):
#         print(i)

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 4- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# numbers = []
# i = 0
# while i < 5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)


# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
# ** ürün sayısını kullanıcıya sorun
# ** dictionary listesi yapısı (name , price) şeklinde olsun
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i = 0
while (i < adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler:
    print(f'ürün adı: {urun["name"]} , ürün fiyatı {urun["price"]} ')




