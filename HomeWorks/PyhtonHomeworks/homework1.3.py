import random
a = '1234567890'
PSW = ''
for x in range(4):
    PSW += random.choice(a)
print(PSW)
