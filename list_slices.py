# list slices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# if the first number in a slice is omitted, its taken to be the start of the list
# if the second number is omitted, its taken to be the end
print("\n\nomitting first and second number")
print(squares[:7])
print(squares[7:])

print("\n\nwith third slice")
print(squares[::2])
print(squares[2:8:3])

# when negative values are used for the first and second values in a slice,
# they count from the end of the list
print("\n\nWITH NEGATIVE VALUES")
print(squares[1:-1])