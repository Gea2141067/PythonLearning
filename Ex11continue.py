for i in range(21):
    if i % 3 == 0 or i % 5 == 0:  # if i is divisible by 3 or 5 the print will be skipped
        continue
    print(i)
