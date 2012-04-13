def divisible(num):
    for i in range(19, 1, -1):
        if num % i != 0:
            return False
    return True
     

if __name__ == "__main__":
    lowest = 20
    while not divisible(lowest):
        lowest += 20
    print(lowest)
