def test():
    print('This is function')
test()

def func(country = 'India'):
    print('This is my country', country)

func('New Zealand')
func()
func('Sweden')

def func2(arg1, arg2, arg3):
    print(arg3 + arg2 + arg1)

func2(arg3 = 'Argument 3', arg2 = 'Argument 2', arg1 = 'Argument 1')

def func3(*test):
    print('The first argument is', test[0])

func3('Hari', 'Krishna', 'Venkata')
