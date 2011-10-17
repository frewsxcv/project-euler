def is_palindrome(i):
    half = len(str(i)) // 2
    if str(i)[:half] == str(i)[-half:][::-1]:
        return True
    return False

largest = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if is_palindrome(i * j) and i * j > largest:
            largest = i * j
print(largest)
