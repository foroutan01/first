
def times(time):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            [func(*args,**kwargs ) for i in range(time)]
        return wrapper
    return my_decorator





@times(6)
def my_func(*args,**kwargs):
    print(args)


my_func("hello_world",x="hello_world")