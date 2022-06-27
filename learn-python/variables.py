x = 'Hi'
y = 345


a, b, c = 'Test', 'dfg', 'asdsdasd'

print(x + str(y) + a + b + c)

# global variable

t = 'testing'

def func():
    global t

    t = 'testing 2'

func()

print(t)