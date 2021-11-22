name = input("What is your name? ")
age = int(input("What is your age?"))
if 18 <= age <= 30:
    print("Welcome to the club Holiday! , {0}".format(name))
else:
    print("Sorry but you do not meet the requirements for club Holiday, {0}".format(name))


