

# 문자열 나누기
'''
a = "abcdefg"
print(a[-1])
print(a[-2:])
print(a[:-2])
print(a[:-1])
'''

# dict 합치기
''''''
from itertools import chain
from collections import defaultdict

dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'C': 2, 'D': 4, 'E': 5}
dict3 = defaultdict(list)
#dict3 = {}
'''
for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)
 
for k, v in dict3.items():
    print(k, v)
'''

for i, j in chain(dict1.items(), dict2.items()):
    print(i, j)
    dict3[i].append(j)


print(dict3)
