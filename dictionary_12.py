# key - value şeklinde çalışır(anahtar-kilit)

# 41 = kocaeli    34 = istanbul gibi

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli']) = 41
# print(plakalar['istanbul']) = 34

# plakalar = { 'key':'value'} şeklinde olucak

# plakalar = {'kocaeli' : 41 , 'istanbul' : 34}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# print(plakalar),

# plakalar['kocaeli'] = 'new value'
# print(plakalar)


users = {
    'sadikturan': {
        'age': 36,
        'roles': ['user'],
        'email': 'sadikturan@gmail.com',
        'address': 'kocaeli',
        'phone': '123456789'
    },
    'denizcumur':{
        'age' : 20,
        'roles': ['admin','user'],
        'email': 'denizcumur@gmail.com',
        'address': 'kocaeli',
        'phone': '123456789'}
}

# print(users['denizcumur']['age'])
# print(users['denizcumur']['email'])
# print(users['denizcumur']['address'])

print(users['denizcumur']['roles'])