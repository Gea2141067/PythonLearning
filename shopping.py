shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

# continues makes everything else in the loop be ignored and continue with the next item

for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

# break will make the loop stop when the if statement is true
