name_card = {'name': '홍길동',
             'tel': '010-1111-2222',
             'address': '부산',
             'email': '1234@1234.com',}


print(name_card)


name_card['etc'] = '이사가능여부','1년 안에'
print(name_card)

print(name_card['address'])
print(name_card['etc'][1])

del name_card['address']
print(name_card)

print(type(name_card))

print(len(name_card))

# print(name_card["address"]) << 삭제했으니 오류가 뜬다

# key in d

print('address' in name_card)
print('address' not in name_card)

# items
# key
# pop, popitem
# reversed
# update
# values

print(name_card.keys())
print(name_card.items())

for k in name_card.keys():
    print(k)
    print('----------')

for v in name_card.values():
    print(v)
    print('----------')

for i in name_card.items():
    print(i)
    
for k,v in name_card.items():
    print(k,v)
    
    
name_card.clear()
print(name_card)
    
print(name_card.get('address'))


s1 = set([1,2,3,2,3])
print(s1)

s2 = set('hello')
print(s2)