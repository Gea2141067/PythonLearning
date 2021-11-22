day = "Friday"
temperature = 30
raining = False

if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

# new code

# This code is unreachable because you cant use if 0 that throws false instantly
# if 0:
#     print("True")
# else:
#     print("False")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
