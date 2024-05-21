names = ['vamshi','varshith','balaji','chiranth']
#print(names)
#print(names[1])
#print(names[-1])

# SLICERS
#print(names[:])
#print(names[2:4])
#print(names[0:3])
#print(names[0:])
#print(names[:4])

# Finding largest element in a list
'''
a=[25,25,4,5]
max=a[0]             #Assume
for i in a:
    if i>max:
        max=i

print("Largest = ",max)
'''

'''
# (or) simple way to do this
a=[2,8,6,20,79,245,36]
a.sort()               # Sorts the numbers in the list in ascending order
print(a[0])
print(a[-1])
'''

# TWO DIMENSIONAL LISTS
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#print(matrix)
#print(matrix[0][1])
#matrix[0][1]=20
#print(matrix[0][1])
'''
for i in matrix:
    for j in i:
        print(j)
'''

# OPERATIONS ON LISTS
a=[5,2,1,7,4]
a.append(20)         # Adds the elements at the end of the list
#print(a)
a.insert(0,10)       # Inserts the elements at the specified index
#print(a)
a.remove(5)          # Removes the element
#print(a)
#a.clear()          # Removes everything inside a list
#print(a)
a.pop()             # Removes the last element in the list
#print(a)
#print(2 in a)
#print(222 in a)
#print(222 not in a)
#print(2 not in a)

a=[1,1,2,3,4,5,5,5,6,67,89,100]
#print(a.count(5))
#print(a.count(25))

b=[7,5,9,3,1,48,165,8654,54,5,685]
b.sort()
#print(b)
b.reverse()
#print(b)

c=b.copy()          # Copies the list
#print(c)
b.append(10)
#print(b)
#print(c)

'''
# Removing the duplicates in the list
a=[1,2,3,1,2,3,4,5,6]
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)
'''