# define function.
def fibonacci(x):
    # return 1 and 0 because there is not two numbers before them.
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        # the equation for fibonacci numbers ( f(n) = f(n-1) + f(n-2) ).
        return fibonacci(x-1) + fibonacci(x-2)


# set range to 21 because we want the sequence till 20.
x = range(21)

print("Fibonacci sequence till 20: ")
for n in x:
    print(fibonacci(n), end=" ")
