# Read number
n_str = input("Введіть натуральне число: ").strip()

max_digit = int(n_str[0])
min_digit = int(n_str[0])

# Find max and min digits
for char in n_str:
    digit = int(char)
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit

diff = max_digit - min_digit
print(f"Максимальна цифра: {max_digit}, Мінімальна цифра: {min_digit}")
print(f"Їх різниця: {diff}")

# Check if even
if diff % 2 == 0:
    print(True)
else:
    print(False)