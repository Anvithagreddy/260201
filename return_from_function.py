# return keyword is used
def max(x,y):
    if x > y:
        return x
    else:
        return y

print(max(4,7))
z=max(8,5)
print(z)

# once we return a value from a function, it immediately stops being executed any code after the return statement
# will never happen
print("\n\n")
def add_numbers(x,y):
    total=x+y
    return total
    print("This won't be printed")
print(add_numbers(4,5))

