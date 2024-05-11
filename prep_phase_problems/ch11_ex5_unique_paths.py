# This problem is known as the unique paths problem: Let’s say you have a grid of rows and columns. Write a function that accepts a number of rows and a number of columns and calculates the number of possible “shortest” paths from the upper-leftmost square to the lower-rightmost square.

# with this solution I am returning only the shortest path, not the count of shortest paths
def shortest_path(row, column):
    if column == 1 and row == 1:
        return 0

    return 1 + min(
        (shortest_path(row, column - 1)) if column > 0 else float('inf'),
        (shortest_path(row - 1, column)) if row > 0 else float('inf')
    )

print(shortest_path(3, 3))

# text solution
def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    # if we are on the same row or column as the target, there is only 1 path
    # this can be our base case

    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

print(unique_paths(3, 3))
print(unique_paths(2, 3))
print(unique_paths(5, 3))
