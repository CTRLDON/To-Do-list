def upper(func):
    def wrapper():
        output = func()
        return output.upper()
    return wrapper

@upper
def osama():
    return "osama"

print(osama())