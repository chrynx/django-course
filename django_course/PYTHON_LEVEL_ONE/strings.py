mystring = 'abcdefg'
print(mystring)
print(mystring[3])
#slicing is [star, end(not including), step of slice]
print(mystring[4:])
print(mystring[:4])
print(mystring[2:5])
print(mystring[::2])
#string is immutable

#methods
print(mystring.upper())
print(mystring.lower())
print(mystring.capitalize())
print(mystring.split())


#print formatting
print("Insert a string here: {}".format("STRING"))
print("Item one: {x} Item Two: {y}".format(x = "A", y = "B"))
