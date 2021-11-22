number = input("Please enter a series of number, using any separators you like: ")
# separators = number[1::4]
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

# This for loop does the same as number[1::4} it just extract all the separators from the numbers

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

# I Added a function to sum the numbers sum()
