# Counting sort:
# Construct a list of counts
# where count[i] is the number of times i appears
# Reconstruct the sorted verison of the list
# using the counts:
# [i]*counts[i] for every i

# my summary: 
# count from smallest to biggest number
# store how many of the same element exists in count
# extend the same amount of counts to get sorted list

# this is only for integers (would have to convert objects to integers otherwise)
def counting_sort(L):
    counts = [0] * (max(L) + 1)
    # c1*max(L) for c2*len(L) for some c1, c2: this has to be proportional to length of list since we count every number to max(L)
    # computing max(L) takes time to prop. to len(L)
    # constructing list of max(L) elems takees time
    # prop. to max(L)

    #c3*len(L) time for some constant c3
    for e in L:
        counts[e] += 1

    # c4*max(L) + c5*len(L)
    # the loop repeats max(L times)
    # we construct a list of size len(L) eventually
    res = []
    for i in range(len(counts)):
        res.extend([i] * counts[i])

    # L[:] = res # copy res over the contents of L
    return res

# The total runtime of counting sort: 
# (c1+c4)*max(L) + (c2+c3+c5)*len(L)

#Complexity: O(len(L) + max(L))

L = [1, 10, 2, 1, 4, 2]
sorted_L = counting_sort(L)

# extension: bucket sort
#            put different elements into buckets
#            sort small buckets separetely 




