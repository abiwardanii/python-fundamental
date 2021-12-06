def new_decorator(func):
    def wrap_func():
        print("Code before executing func")
        func()
        print("Code after executing func")
    return wrap_func

# tanpa decorator
# def func_needs_decorator():
#     print("I want to be decorated")
# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()


# Decorator
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
func_needs_decorator()