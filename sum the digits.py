def sum_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_digits((num - num % 10) / 10)

print(sum_digits(3243))
