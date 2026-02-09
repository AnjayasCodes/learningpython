num_pad = ((1, 2, 3), (4, 5, 6),
           (7, 8, 9), ("*", 0, "#"))
for lists in num_pad:
    for list in lists:
        print(list, end="")

    print()
