# generate An random points
# keep track of Am: the number of points inside
#                   the unit quarter-circle
# compute 4*Am/An

import random

def inside_unit_circle(x, y):
    ''' Return True if (x, y) is a coordinate
    inside the unit circle'''
    r_sq = x**2 + y**2
    return r_sq < 1

def estimate_pi(N):
    '''Estimate pi using N random points'''
    Am = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if inside_unit_circle(x, y):
            Am += 1

    return 4*Am/N

if __name__ == '__main__':
    print(estimate_pi(1000))
