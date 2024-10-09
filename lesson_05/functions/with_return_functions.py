def add(a, b):
    if a > 5:
        print(a + b)
        return a + b
    if a < 5:
        return 25



result = add(3, 3)
print(result)


def calc(a, b):
    return (a + b), (a * b)

result = calc(5, 6)
print(result)


