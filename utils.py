
def pass_input(get_input):
    def wrapper(func):
        def exec(day, *args, **kwargs):
            return func(get_input(day), *args, **kwargs)
        return exec
    return wrapper
