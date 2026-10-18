count = 0
# Read first number
prev = int(input("Введіть число (0 для завершення): "))

# Process sequence
while True:
    current = int(input("Введіть наступне число: "))
    if current == 0:
        break
    if prev > current:
        count += 1
    prev = current

print("Кількість елементів, які більші за наступний:", count)