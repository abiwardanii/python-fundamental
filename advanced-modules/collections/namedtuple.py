from collections import namedtuple
bunny = namedtuple('bunny', ['name', 'age', 'color'])
bun = bunny(name='bun', age=1, color='white')
print(bun)
print(bun.name)
print(bun.age)
print(bun.color)