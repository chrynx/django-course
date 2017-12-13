mylist = ['a','b','c','d','e']
list_two = ['x','y','z']
numlist = [1,6,5,7,5,4]
#adds a list instead of individually
mylist.append(list_two)
#adds the elements inside the list individually
mylist.extend(list_two)
print(mylist)
item = mylist.pop(0)
print(mylist)
print(item)
mylist.reverse()
print(mylist)
numlist.sort()
print(numlist)
mylist = [1,2,['x','y','z']]
print(mylist[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
