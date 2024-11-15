# name = 'sadık turan'

# for letter in name:
#     if letter == 'ı':
#         continue
#     print(letter)
# break döngüden direkt çıkış yapar ama continue sadece o anki döngü 
# turunu iptal eder kalan kısmı devam ettirir.

# x = 0
# while x<5:
#     x += 1
#     if x == 2:
#         # break
#         continue
#     print(x)



# 1-100 e kadar tek sayıların toplamı

x = 0
result = 0
while x <= 100:
     x += 1
     if x % 2 == 0: 
      continue
     result += x
print(f'toplam : {result}')
# x = 1
# result = 0
# while x <= 100:
#     result += x
#     x += 1
# print(f'toplam : {result}')

    