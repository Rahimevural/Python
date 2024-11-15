numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

# val = min(numbers)
# val = max(numbers)
# val = max(letters)
# val = min(letters)

val = numbers[3:6]

numbers[4] = 40 

# numbers.append(49)
# numbers.insert(3, 78)#istenilen yere ekler 

# numbers.pop(0)#eleman siler
# numbers.pop(-1)
# numbers.remove(5)#karakter siler indeksi değil karakterin kendisini yazarak silinir
numbers.sort()#listeyi küçükten büyüğe sıralar
letters.sort()
numbers.reverse()#listeyi büyükten küçüğe sıralar
letters.reverse()#lşisteyi tersten sıralar


print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))#istediğimiz elemanın kaç tane olduğunu sayar

print(letters.count('a'))

numbers.clear()
print(numbers)
