#
# d = {
#     key: value
# }

d = {
    1: 'first',
    2: 'second',
    'etc': 'etc'
}

list1 = [['a,', 1], ['b', 2], ['c', 3]]
dic = dict(list1)
print(dic, type(dic))

dic1 = {}

d4 = dict.fromkeys(['a', 'b', 'c'], 100)
print(d4, type(d4))

person = {}

s = "Ivanov Ivan Odessa Marselskaya_49 23.04.1986"
listS = s.split(" ")

person['lastName'] = listS[0]
person['firstName'] = listS[1]
person['city'] = listS[2]
person['street'] = listS[3]
person['date'] = listS[4]

print(person)

s1 = "Samoylov Stepan Odessa Marselskaya_11 09.11.1999"
listS = s1.split(" ")

listOfDict = []
listOfDict.append(person)
print("Create List of Dictionary")
print(listOfDict)

person['lastName'] = listS[0]
person['firstName'] = listS[1]
person['city'] = listS[2]
person['street'] = listS[3]
person['date'] = listS[4]

listOfDict.append(person)
print(person)
