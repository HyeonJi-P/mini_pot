# 파이썬 문법 테스트 장소

# 문자열 나누기
'''
a = "abcdefg"
print(a[-1])
print(a[-2:])
print(a[:-2])
print(a[:-1])
'''

# dict 합치기
'''
from itertools import chain
from collections import defaultdict

dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'C': 2, 'D': 4, 'E': 5}
dict3 = defaultdict(list)
#dict3 = {}

for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)
 
for k, v in dict3.items():
    print(k, v)

for i, j in chain(dict1.items(), dict2.items()):
    print(i, j)
    dict3[i].append(j)
print(dict3)
'''

# 리스트 문자열 삭제하기
'''
import re
a = (('time',), ('plant',), ('temperature',), ('humidity',), ('illuminance',))
a = list(a)

print(type(a))
print(a)

clear_str = "()',"
for i in range(0, len(a)):
    a[i] = str(a[i])
    a[i] = ''.join(_ for _ in a[i] if _ not in clear_str)

print(type(a))
print(a)

print(type(a[0]))
print(a[0])
'''

# sql 쿼리 문자열 처리하기
''''''
class a:
    @staticmethod
    def insert(insert_data):
        print(insert_data)


dict_message = {
    'time' : '1111-22-33 44:55:66',
    'plant' : 'baechu',
    'temperature': 21,
    'humidity': 6,
    'illuminance': 24.13
}

a.insert(dict_message)











