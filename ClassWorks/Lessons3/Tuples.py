

a = (1, 2, 3, 4, 5)
print(a, type(a))
b = (6, 7, [10, 20, 30])
print(b, type(b))


b[2].append(100)
print(b, type(b))


print(len(a))

print(2 in a or 5 in a and 3 in a)

print(a + b, b + a)

print(sum(a))

print(a.index(2))

a.count(4)

print(a.__sizeof__())

# you can't change tuple after init
# but you can make changes if you transform it to list

list1 = list(a)
print(list1, type(list1))
list1.append(10)
a = tuple(list1)
print(a, type(a))

