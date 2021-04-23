# syntax:
# if condition:
#    statements

print("SIMPLE IF STATEMENT")
x = 42
if x > 5:
    print("x is greater than 5")


# if within if
print("\n\nIF WITHIN IF")
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("between 5 and 47")