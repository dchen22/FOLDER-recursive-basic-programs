def sum_natural(num):
    if num == 0:
        return num
    if num > 0:
        return num + sum_natural(num - 1)

print(sum_natural(100))