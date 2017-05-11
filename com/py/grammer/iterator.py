from collections import Iterator, Iterable

a = isinstance([],Iterable)
print(a)

print(isinstance(iter([]),Iterator))

print(isinstance('aaa',Iterable))

print(x for x in range(10))

print(isinstance((),Iterable))

print(type(range(10)))
