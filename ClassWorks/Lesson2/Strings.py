print('Text')

# "hello world
# frineds" >>> That won't work

# Do like this
a = '''hello
world
and dimensions
'''
print(a)
# The same
a = """hello
world
and dimensions
"""
print(a)

# r = input()
q = ''
q = " "
# print(r)

# Concatenation
s = 'he'
s1 = 'llo'
s2 = 'world'

print(s + s1 + " " + s2)
print(s + s1 + "\n" + s2)
print(s + s1 + "\t" + s2)
print(s * 3)
# print(s + 3) error you can't concat boolean with
# but you can
print(s + str(3))
# also you cant to print(s * 3.5)
print(s + str(3.5))

# Methods
s = """There has been a lot of research which shows the importance
 of physical health in avoiding anxiety and depression. The mind 
 and the body are highly interconnected. We can all make fairly
  easy changes in our lifestyle to include more exercise, healthier 
  eating, getting enough sleep, being exposed to sunlight and so on.
   Research into exercise has found that it has a positive impact on mood. 
   Physical activity stimulates the release of endorphins in the brain to produce the feel-good factor.
    Sleep is vitally important for children and adolescents to help concentration levels.
     A good night’s sleep also stops people being bad-tempered and flying off the handle."""
print(s.upper())
print(s.lower())
print(s.count('h'))
print(s.find('e'))
print(s.index('o'))
# if index wont find a symbol he will throws an exception
print("len is___")
print(len(s))
print(s.isalpha())
print(s.upper().lower())

print('AAA' == 'aaa')


