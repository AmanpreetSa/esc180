# sort a list of integers
# [5, 10, 12, 3, 2, 1, 100]
# want to sort the list

# Algorithm: "Selection sort"
# pick the largest element, put it in position n
# pick the next largest element, put it in position n-2
# pick the next largest element, put it in position n-3

# [5, 10, 12, 3, 2, 1, 100]             iterate through whole list: 100 is in largest position         
# [5, 10, 12, 3, 2, 1, 100]             ... now we find 12 but go up to only 1 this time
# [5, 2, 1, 3, 10, 12, 100]             ... put 12 in right spot, iterate through, but now go up to 10
# [3, 2, 1, 5, 10, 12, 100]             
# [1, 2, 3, 5, 10, 12, 100]
# [1, 2, 3, 5, 10, 12, 100]

def selection_sort(L):
    for i in range(len(L)-1):
        cur_max = L[0]
        cur_max_j = 0
        for j in range(len(L)-i):
            if L[j] > cur_max:
                cur_max = L[j]
                cur_max_j = j
        # cur_max_j is the location of theelemtn we need need to swap to the right
        L[cur_max_j], L[len(L)-i-1] = L[len(L)-i-1], L[cur_max_j]

# How many times does the linner loop run?
# n = len(L)

# n + (n-1) + (n-2) + ... + 1 times
#                   = n(n+1)/2 times
#                   = n^2/2 + n/2 times proportional to n^2 for large n

# Selection sort runs in O(n^2) time
#                        n + len(L)


# how it works (memorize!): 1 + 2 + 3 + 4 + ... + k = k(k+1)/2

