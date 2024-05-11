
count = 0
def fib(n, memo = {}):
    global count
    count += 1

    if n == 0 or n == 1:
        return n

    if n not in memo:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    return memo[n]


fib(20)
print(count)
