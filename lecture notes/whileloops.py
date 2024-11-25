m = 15
n = 100
step = 17

for i in range(m, n, step): # runs approx. (n-m)/step
    print(i)

# m
# m + step
# m + 2*step
# ...
# n (not including n)

i = m
while i < n:    # keep going until it stop being
                # the case that i < n
    print(i)
    i += step

# i = 15, 15+17, 15+17*2, ...., 83

# will stop when i becomes not smaller than 100
print(i)
