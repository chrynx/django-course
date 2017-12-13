#LOCAL
lambda x: x**2

#Enclosing Function Locals
name = 'This is a global name!'

def greet():
    name = 'sammy'

    def hello():
        print('hello ' + name )
    hello()
greet()


x = 50

def func():
    global x
    x = 1000

print('before', x)
func()
print('after', x)
