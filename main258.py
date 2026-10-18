# Read terms count
n = int(input("Введіть кількість членів ряду n: "))

pi_approx = 0
sign = 1

# Leibniz formula loop
for i in range(n):
    term = 4 / (2 * i + 1)
    pi_approx += sign * term
    sign *= -1

print("Результат обчислення числа Пі:", pi_approx)