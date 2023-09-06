#  *
# ***
#  *

# n = 2

#  *
# ***
# *****

n = int(input("n = "))

for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end="")
    for k in range(0, 2 * i - 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for k in range(0, 2 * i - 1):
        print("*", end="")
    print()
