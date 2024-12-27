# Task 1
a = [7, -10, 5, -8, 0, 10, 1, 3, 6, 7]
n = len(a)
for i in range(0, n - 1):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)


# Task 2
strings = ["Bulat", "Rayana", "Regina", "Lily", "Alesha", "Ksusha", "Morgenshtern", "Kate", "koshka", "sobaken", "meow"]
sorted_strings = sorted(strings, key=len)
print(sorted_strings)


# Task 3
a = [7, -10, 5, -8, 0, 10, 1, 3, 6, 7]
n = len(a)
for i in range(0, n - 1):
    for j in range(0, n - 1):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
