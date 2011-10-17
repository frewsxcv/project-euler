# digit(): splits an integer into a list of sorted digits
digit = lambda i: sorted(str(i))

i = 1
while True:
    if digit(i) == digit(2 * i) == digit(3 * i) == digit(4 * i) == \
     digit(5 * i) == digit(6 * i):
        break
    i += 1
print(i)