s = "GLOBAL VARIABLE"
def func():
    global s
    s = 50
    print(s)

func()
