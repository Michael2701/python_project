from functools import wraps

def not_null(func):
    def wrapper(*args, **kwargs):
        if all([arg != None for arg in args]):
            func(*args, **kwargs)
            print('from not_null function')
            return True
        print("Argument can not be empty")
        return False
    return wrapper


def is_number(func):
    def wrapper(*args, **kwargs):
        is_valid_number = True
        message: str = ""

        for arg in args:
            if type(arg) != int and type(arg) != float:
                message = f"The argument '{arg}' is not valid number"
                is_valid_number = False
                break

        if is_valid_number:
            func(*args, **kwargs)

        print(message)
        return is_valid_number
    return wrapper

def a():
    pass

def b(a):
    print("")
    a()


#decorator factory
def length(min:int, max:int):
    #decorator
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            is_valid_length = True
            message: str = ""
            if all([ arg != None and isinstance(arg, str) for arg in args]):
                for arg in args:
                    if min > len(arg):
                        message = f"String have to be at least {min} chars"
                        is_valid_length = False
                        break

                    elif max < len(arg):
                        message = f"String have to be less or equal to {max} chars" 
                        is_valid_length = False
                        break

                if is_valid_length:
                    function(*args, **kwargs)
            else:
                message = f"Not valid string (type error)"
                is_valid_length = False

            print(message)
            return is_valid_length
        return wrapper
    return decorator


def is_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_valid_string = True
        message: str = "is_string "

        for arg in args:
            if not isinstance(arg, str):
                message = f"The argument '{arg}' is not valid string"
                is_valid_string = False
                break

        if is_valid_string:
            return func#(*args, **kwargs)

        print(message, is_valid_string)
        return is_valid_string
    return wrapper

def is_number(func):
    def wrapper(*args, **kwargs):
        is_valid_number = True
        message: str = ""

        for arg in args:
            if type(arg) != int and type(arg) != float:
                message = f"The argument '{arg}' is not valid number"
                is_valid_number = False
                break

        if is_valid_number:
            func(*args, **kwargs)

        print(message)
        return is_valid_number
    return wrapper


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# @is_string
# @length(min=3, max=15)
@is_number
def set_first_name(name:str):
    global first_name
    first_name = name


@percent
def printer(msg:str):
    print(msg)

name = 'as'
# name = 123
first_name: str = "huy"

# print(set_first_name(name))
if set_first_name(name):
    printer(msg=f"Hello {first_name}")

foo1(*args1)
foo2(**args2)
