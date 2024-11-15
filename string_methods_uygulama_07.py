website = "http://www.sadikturan.com"
course = "python Kursu: baştan sona python programlama rehberiniz(40saat)"


# 1- ' Hello Word ' ifadesinin baş ve sondaki boilukı karakterlerini silin
result = ' Hello Word '.strip()
print(result)
result = ' Hello Word '.lstrip() #soldaki boşluğu siler
result = ' Hello Word '.rstrip() #sağdaki boşluğu siler
result = website.lstrip('/:pth') # bu şekildede istediğimiz karakterleri sileriz
# karakteri bir kez yazmak yeterli olur.

# 2- 'www.sadikturan.com ' içindeki sadıkturan haricindeki her karakteri silin
result = 'www.sadikturan.com '.strip('w.moc')

# 3- 'course' tum karakterleri küçük haraf yap
result = 'course'.lower()
result = 'course'.upper()

# 4- 'website' içinde kaç tane a karakteri var (count('a'))
result = website.count('a')
result = website.count('www',0,10) #istediğimiz aralığı belirtebiliriz
# eğer bu aralıkta varsa kaç tane olduğunu yazdırır.

# 5- 'website ' wwww ile başlayıp com ile bitiyor mu
result = website.startswith('www')
result = website.startswith('http')
result = website.endswith('com')
# 6- 'website ' içinde '.com' ifadesi var mı
result = website.find('com')
result = website.index('com')


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi (isalpha,isdigit)
result = course.isalpha()
result = 'hello'.isalpha()
result = course.isdigit() # rakammı diye sorar
result = '123'.isdigit()


# 8- 'contents' ifadesini satoırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result = 'contents'.center(50,'*')
result = 'conters'.ljust(50,'*')
result = 'contents'.rjust(50,'*')

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
result = course.replace(' ','-') #virgül koyup rakam yazarak sınırlandırabiliriz

# 10- 'Hello Word' karakter dizisinin 'word' ifadesini 'There' olarak değiştirin 
result = 'Hello Word'.replace('Word','There')

# 11- 'course' karakter dizisini boşluk karalterlerinden ayırın
result = course.split(' ')

print(result)