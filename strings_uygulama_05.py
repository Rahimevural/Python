# website = "http://www.sadikturan.com"
# course = "python kursu: Baştan sona pyhton programlama rehberiniz(40 saat)"

# 1 - course karakter dizisinde kac karakter var?
# uzunluk = len 
# print(uzunluk(course))
# result = len(course)
# print(result)


# 2 - website içinden www karaketerlerini alın
# print(website[7:10])
# result = website[7:10]
# print(result)


# 3 - website içinden com karakterlerini alın
# print(website[-3:])
# lenght = len(website)
# result = website[lenght-3:lenght]
# print(result)


# 4 - course içinden ilk  15 ve son 15 karakterlerini alın
# print(course[0:15])
# print(course[:15])
# print(course[-15:])
# 5 - course ifadesindeki karakterleri tersten yazdırın
# result = course[::-1]
# print(result)

# s = '12345' * 5
# print(s[::5])






name, surname, age, job ='Bora', 'Yılmaz', 32, 'mühendis'

 # 6- yukarıdakı verilen ifadeler ile ekrana aşağıdaki ifadeyi yazdırın
       #'Benim adım Bora Yılmaz , Yaşım 32 ve mesleğim mühendis.'

# result = 'benim adım ' +  name  +  ' '  +  surname  + ' , yaşım ' +  str(age)  + ' ve mesleğim ' + job
# print(result)
# result = 'Benim adım {} {} , yaşım {} ve mesleğim {}.'.format(name ,surname, age, job)
# print(result)
# result =f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}."
# print(result)

  # 7- 'Hello word' ifadesindeki w harfini W ile değiştirin.
# result = 'Hello Word'
# result = result[0:6] + 'W' +result [-3:]
# print(result)

  
  
  # 8- 'abc' ifadesini yan yana 3 defa yazdırın 
# result = 'abc'
# print(result *3)  