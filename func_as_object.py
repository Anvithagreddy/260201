def multiply(x, y):
    return x * y
a=4
b=7
operation = multiply
print(operation(a,b))

# functions can also be used as arguments of there functions
print("\n\n")
def add(x, y):
    return x+y

def do_twice(func, x, y):
    return func(func(x,y),func(x,y))

a=5
b=5
print(do_twice(add,a,b))