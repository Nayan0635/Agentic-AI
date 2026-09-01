numbers = [0, 2, 0, 3, 0, 4]
print(numbers)

j = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[j] = numbers[i]
        j+= 1
while j < len(numbers):
    numbers[j] = 0
    j+= 1
print(numbers)