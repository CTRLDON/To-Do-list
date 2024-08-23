def upper(func):
    output = func()
    return output.upper()

@upper()
def osama():
    return "osama"

print(osama())