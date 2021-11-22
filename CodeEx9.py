for i in range(0, 101):
    if i % 7 == 0:
        print(i)

print()

# other solutions
for i in range(0, 101, 7):
    print(i)

print()

for i in range(101)[::7]:
    print(i)
