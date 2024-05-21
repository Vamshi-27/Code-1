# Loops : while , for

'''
i=1
while i <= 5:
    print(i)
    i += 1
print("Done")
'''

'''
i=1
while i <= 5:
    print('*'*i)
    i += 1
print("Done")
'''

#for i in range(0,4,1):
    #print('*'*i)

#for i in "Python":
    #print(i)

#for i in range(0,11,2):
    #print('*'*i)

'''
price = [10,20,30]
total=0
for i in price:
    total += i
print(f"Total:{total}")
'''

# Generating Coordinates
'''
for i in range(4):
    for j in range(3):
        print(f'({i},{j})')
'''

'''
n = [5,2,5,2,2]

for i in n:
    #print('*'*i)     # Simple way to do this
    output = ''
    for j in range(i):
        output += '*'
    print(output)
'''

