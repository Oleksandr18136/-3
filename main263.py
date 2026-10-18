n = int(input("Введіть кількість днів спостереження: "))
min_temp = float('inf')
below_minus_15 = False

# Find min temp
for i in range(n):
    temp = float(input(f"Введіть температуру для дня {i + 1}: "))
    if temp < min_temp:
        min_temp = temp
    if temp < -15:
        below_minus_15 = True

formatted_min = int(min_temp) if min_temp == int(min_temp) else min_temp

print("Найнижча температура:", formatted_min)

if below_minus_15:
    print("Yes")
else:
    print("No")