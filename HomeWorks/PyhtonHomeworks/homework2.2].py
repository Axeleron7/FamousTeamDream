a = "Аббревиатура"
print(a)

a = list(a)
print(a)
del a[0]
del a[6]
del a[9]
print(a)
a = "".join(a)
print(a)