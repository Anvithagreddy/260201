# Break
# to end a while loop prematurely, we can use a break
print("BREAK STATEMENT")
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

# Continue
# Another statement that can be used within loops is continue
print("\n\nCONTINUE STATEMENT")
i=1
while i<=5:
    print(i)
    i+=1
    if i==3:
        print("Skipping 3")
        continue