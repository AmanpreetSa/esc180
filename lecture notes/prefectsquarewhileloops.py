# perfect square: a number whose sqrt is an integer
# want to know: how many perfect squares are there that are <= n

# n = 10
# 0, 1, 4, 9
# 4 perfect squares smaller than 10

def is_perfect_square(k):
    '''Return True if and only if k is a perfect square
    '''

    # for i = 0, 1, 2, 3, 4, ....,k
    # if i**2 == k, return True
    for i in range(0, k+1):
        if i**2 == k:
            return True
    return False

def count_perfect_squares(n):
    '''Return the number of perfect squares <= n'''

    count = 0
    for j in range(0, n+1):
        if is_perfect_square(j):
            count += 1
    return count