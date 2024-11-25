for i in range(n):
    for j in range(100):
        pass

# O(n): scaling over the other for loop it's relative to it (linear)
# if it was "for j in range(n)" as well, then it would be O(n^2) time complexitity

def binary_search(L, e):

    low = 0
    high = len(L)-1
    while high-low >= 2:
        # 2 comparisons
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid
        
    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    else:
        return None
    
# The simple form of the asymptotic worst-case runtime complexity (tight upper bound) (Friday Nov 22)
# this means: in the worst case, what is the runtime proportional to (if you don't return early)

# technically: t(n) = n^2 is O(n^n^n) but it asks for TIGHT UPPER BOUND (can't do this)
#                       for large n, a*n^2 <= b*n^n^n
#                            for any a, b

# worst case definition: given input of size n, the worst case would end or start of list
# for bin search (worst possible output choice)
# simple form definiton: don't say (50n), say O(n)
# runtime complexiity: what matters is when low and high become either the same or have a difference of 1

# high-low starts as n-1, n = len(L)
# becomes ~ n/2
# ... n/4
# ... n/8
# ...

# for large n, binary search runs in time proportional to log2(n), n = len(L)
# Meaning: runtime is ~constant*log2(n) ms

# approx log2(n) iterations to go from n-1 to 1 if we halve the range low...high every iteration


#log_y(x) = log(x)/log(y) proportional to (1/log(y))*log(x) - log(x)