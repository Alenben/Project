def strupr(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
@strupr
def printstr1():
    return "good evening"
print(printstr1())
