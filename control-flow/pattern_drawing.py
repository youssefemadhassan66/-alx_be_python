# Pattern Drawing with While and For Loops
size = int(input("Enter the size of the pattern: "))

for row in range(size):
    for col in range(size):
        print("*", end="")
    print()
