# list operations
print("List operations")
nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)

# to check if an item is in a particular list, we can use the in operator
# it returns True if the item occurs one orr more times in the list, and False if iit doesn't
print("\n\nIN OPERATION")
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

print("\n\n\nANOTHER EXAMPLE")
nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
