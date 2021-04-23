# syntax:
# if condition:
#   statements
# else:
#   statements

x = 4
if(x == 5):
    print("YES")
else:
    print("NO")

# every if block can have only one else statements

num = 3
if num == 1:
    print("one")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")