def is_palindrome(num):
    str_num = str(num)
    half = len(str_num) // 2
    if str_num[:half] == str_num[-half:][::-1]:
        return True
    return False

if __name__ == "__main__":
    largest = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            if is_palindrome(i * j) and i * j > largest:
                largest = i * j
    print(largest)
