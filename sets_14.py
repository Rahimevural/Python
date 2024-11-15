fruits = {'orange','apple','banana'}

print(fruits)
# Normal listeden farkı bu listeye indeks numarası 
# kullanarak ulaşılmaz
# liste sıralanamaz
#liste içinde her elemandan sadece bir tane olur
# print(fruits[0]) şeklinde indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape'])
fruits.remove('mango')
fruits.discard('applee')# istenilen elemanı siler
fruits.pop()
fruits.clear()
print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))