n = 1000

def log10(b):
    global n
    count = 0
    while n > 1:
        n //= 10    # n = n // 10
        count += 1
    return count

# after the while loop, count is the number of times
# we needed to divide by 10 in order to get to 1

if __name__ == '__main__':
    n = 1000000
    print(log10(n))

