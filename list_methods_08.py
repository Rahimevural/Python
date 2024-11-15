# 1- "bmw , mercedes , opel , mazda" elemanlarına sahip bir liste oluşturun
arabalar = ['bmw','mercedes','opel','mazda']
# 2- liste kaç elemanlıdır?
result = len(arabalar)
# 3- listenin ilk ve son elemanı
result = arabalar[0]
result = arabalar[-1]
# 4- mazda değerini toyota ile değiştir 
arabalar[-1]= 'toyota'
result = arabalar
# 5- mercedes listenin bir elemanı mıdır
result = 'mercedes' in arabalar
# 6- listenin -2 indeksindeki değer nedir
result = arabalar[-2]
# 7- listenin ilk üç elemanını alın 
result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]
# 8- listenin son iki elemanı yerine "toyota" ve "renault" değerlerini ekleyin 
arabalar[-2:] = ['toyota','renault']
result = arabalar
# 9- listenin üzerine "audi" ve "nissan" değerlerini ekleyin
result = arabalar + ['audi','nissan']
# 10- listenin son elemanını silin
del arabalar[-1]
result = arabalar
# 11- liste elemanlarını tersten yazdırın 
result = arabalar[::-1]
# 12- Aşağıdaki verilenleri bir liste içinde saklayın

      # studentA: yiğit bilgi 2010, (70,60,70)
      # studentB: sena turan 1999, (80,80,70)
      # studentC: ahmet turan 1998, (80,70,90)

studentA = ['yiğit' ,'bilgi',2010,[70,60,70]]
studentB = ['sena', 'turan',1999,[80,80,70]]
studentC = ['ahmet','turan',1998,[80,70,90]]

# 13- liste elemanlarını yazdırın
result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)