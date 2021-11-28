options = [1, 2, 3, 4, 5, 0]
statements = ["Learn Python", "Learn Java", "Go swim",
              "Have dinner", "Go to bed", "Exit"]
user_choice = ""
while user_choice not in options:
    print("Please choose your option from the list below")
    for i in options:
        print("{}\t{}".format(options[i - 1], statements[i - 1]))
    user_choice = int(input())
else:
    if user_choice != 0:
        print("You select option {} that is {}"
              .format(options[user_choice - 1], statements[user_choice - 1]))
