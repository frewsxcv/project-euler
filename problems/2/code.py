def fibonacci():
    x, y = 0, 1
    while True:
        x, y = y, x + y
        if y > 4000000:
            return
        yield y

print(sum([i for i in fibonacci()][1::3]))
