from collections import defaultdict
d = defaultdict(lambda: 0) # contoh value default
d['a'] = 1
print(d['a'])
d['ngasal']
print(d['ngasal']) # output: 0 karena defaultdict tidak memiliki key 'ngasal'