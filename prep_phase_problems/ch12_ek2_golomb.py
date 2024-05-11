def golomb(n, memo={}):
    if n == 1:
        return 1

    memo[n] = memo.get(n, 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo))

    return memo[n]

def orig_golomb(n):
    if n == 1:
        return 1

    return 1 + orig_golomb(n - orig_golomb(orig_golomb(n - 1)))

print(golomb(30))
print(orig_golomb(30))
