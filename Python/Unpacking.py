coordinates=[1,2,3]
# we can access these by their indices
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

# OR 

x,y,z=coordinates             # This is called as unpacking
print(x*y*z)


# Same for tuples
b=(4,5,6)

d,e,f=b
print(d*e*f)