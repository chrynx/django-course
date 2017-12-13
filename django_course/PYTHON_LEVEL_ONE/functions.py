def hello():
    return 'hello'

result = hello()
print(result)

def addNum(num1,num2):

    return num1+num2

result = addNum("2", "3")

print(type(result))


#Lambda Expression
#Filter
my_list = [1,2,3,4,5,6,7,8]


evens = filter(lambda num: num%2 == 0,my_list)
print(list(evens))
