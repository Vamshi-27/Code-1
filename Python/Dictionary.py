# We can define a dictonary with curly braces
'''
customer={'name':'Vamshi','age':20,'is_good':True}          # always contains a key value pair
#customer={'name':'Vamshi','age':20,'age':21,is_good':True}    #ERROR - a dictionary should contain unique keys, but values may be same     

print(customer['name'])       # Accessing values with the help of keys
#print(customer['birth_date'])     # Key-Error

#print(customer.get('name'))
#print(customer.get('birth_date'))      # Returns None if key is not present
#print(customer.get('birth_date','27-Mar-2004'))   # Returns the date which is specified (dosen't modify the dictionary)
#print(customer)

customer['dob']='27-Mar-2004'     # gets added to the dictionary
print(customer['dob'])

print(customer)
'''

