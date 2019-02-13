n = int(input("Introduce a number: "))
sum = 0

for i in range(0, n + 1, 1):
    sum = sum + i
print("The sum of the numbers from 1 to", n, "is:", sum)