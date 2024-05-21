# Tuples are similar to lists, but we cannot modify the tuples (ie.,tuples are immutable)

a=(1,2,3)
#print(a.count(1))
#a[0]=10             # ERROR - Cannot modify tuple

b=list(a)
#print(b)         # Converting a tuple into a list

c=[1,8,54,7,8]
d=tuple(c)
#print(d)            # Converting a list into a tuple