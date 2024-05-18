#print("Vamshi")

a=10
#print(a)

a="vamshi"
#print(a)

b="vamshi's laptop"
#print(b)

c='vamshi"s mobile'

# Multi line string
d='''                                             
hi ram

here is my first email to you

Thank you
The support team

'''
#print(d)


ab='Python'
#print(ab[0])
#print(ab[-1])
#print(ab[0:3])
#print(ab[0:])
#print(ab[:3])
#print(ab[:])

fa='john'
la='smith'
m=fa + '[' + la + '] is a coder'         # +-->Concatenation
#print(m)

g = f'{fa} [{la}] is a coder'          # f-string
#print(g)

# String methods
a='vamshi'
#print(len(a))                         # gives length of the string

#print(a.upper())
#print(a.lower())

#print(a.find('v'))      # gives the index of specified letter(it is case-sensitive) (returns -1 if the letter is not present in the string)

b='Python Course'
#print("Length of b:",len(b))
b=b.replace('Course','Learning')
#print("Length of b:",len(b))

c='vamshi'
#print('v' in c)
#print('d' in c)
#print(c.title())          # returns first letter as then upper case

# Arithmetic operations
#print(10+3)
#print(10-3)
#print(10*3)
#print(10 / 3)             # returns float when it gets operated
#print(10 // 3)            # returns int when it gets operated
#print(10%3)              # returns remainder
#print(10**2)           # exponent

x=10
x=x+3
#print(x)

y=10
y += 3            # augumented assignment operator  works as y=y+3
#print(y)

z = 10 + 3 * 2 ** 2
#print(z)                 # order: parenthesis , ** , * (or) / , + (or) -