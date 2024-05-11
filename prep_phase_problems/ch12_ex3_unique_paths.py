def unique_paths(rows, columns, memo = {}):
    if rows == 1 or columns == 1:
        return 1

    memo[(rows, columns)] = memo.get(
        (rows, columns),
        unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
    )

    print(memo)
    return memo[(rows, columns)]

print(unique_paths(3, 5))
