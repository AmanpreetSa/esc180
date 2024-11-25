# recursion: function calling itself

# defintion of n factorial
# n! = 1*2*...*n
# n! = (n-1)! * n

def fact(n):
    if n == 0:              # need base case
        return 1            # for a simple input without a recursive call
                            # ie. without func calling itself
                            
    return n * fact(n-1)    # if a recursive fucntion, we need a recursive step
                            # the output in terms of the function itself
                            # but with a "simpler" input (smaller input in this case)

# The three rule of writing recursive functions:
# 1. Recursive step: to get the answer you must know the answer (where func calls itself with a
#    simpler or smaller verison of the problem)
# 2. Base case: condition where the recursion stops otherwise func would call itself indefinitely
# 3. Progress Towards Base Case: ensure each recursive  call modifies the input so it eventually 
#    satisfies the base case condition (i.e: reducing number, slicing a list, updating a state)

print(fact(5))

# Example:

# fact(0)
# |           \ 1
# fact(1)
# |           \ 1
# fact(2)
# |           \ 1 * 2
# fact(3)
# |           \ 1 * 2 * 3
# fact(4)
# |           \ 1 * 2 * 3 * 4
# fact(5)
#            \ 1 * 2 * 3 * 4 * 5



