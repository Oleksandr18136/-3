# Read size
n = int(input("Введіть розмір шаблону (число n): "))

# Print triangle of stars
for i in range(n, 0, -1):
    print("*" * i)

print("Шаблон побудовано успішно!")