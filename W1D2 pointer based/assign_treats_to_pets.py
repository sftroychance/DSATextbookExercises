# Imagine you're a pet owner wanting to give treats to your pets. Each pet has a specific appetite level represented by an array appetite[i], which is the minimum size of a treat the pet will be happy with. Each treat has a size represented by an array treats[j]. A pet will be satisfied if the size of the treat treats[j] is greater than or equal to its appetite level appetite[i]. Your goal is to maximize the number of satisfied pets and output the number of satisfied pets in the end.

# P
# appetite array is minimum size of treat for that pet
# treats array is size of each treat
# sort the arrays
# two pointers, one on each array - treat_ptr, appetite_ptr, both at 0
# while appetite_ptr < len(appetites) and treat_ptr < len(treats)
# - increment treats pointer until treat value >= current appetites value or treat_ptr >= len(treats)
# - increment count
# - increment both pointers
# return count

# time: O(AlogA + TlogT) - A is size of appetites array, T is size of treats array
# space: O(1) -> no data structures created

def assign_treats(appetites, treats):
    appetites.sort()
    treats.sort()

    treat_ptr = 0
    appetite_ptr = 0
    count = 0

    while appetite_ptr < len(appetites) and treat_ptr < len(treats):
        if treats[treat_ptr] >= appetites[appetite_ptr]:
            count += 1
            appetite_ptr += 1

        treat_ptr += 1

        # original solution, less elegant - checking treat_ptr in range 3 times total!
        # problem is that we can increment treat_ptr more than once within larger while loop, so we have to keep checking the treat_ptr
        # while treat_ptr < len(treats) and treats[treat_ptr] < appetites[appetite_ptr]:
        #     treat_ptr += 1

        # if treat_ptr < len(treats):
        #     count += 1
        #     treat_ptr += 1
        #     appetite_ptr += 1

    return count

print(assign_treats([3, 4, 2], [1, 2, 3]) == 2)
print(assign_treats([1, 5], [5, 5, 6]) == 2)
print(assign_treats([1, 2, 3], [3]) == 1)
print(assign_treats([2], [1, 2, 1, 1]) == 1)
print(assign_treats([4, 3, 1], [2, 1, 3]) == 2)
print(assign_treats([1,2,3], [1,2,3]) == 3)
print(assign_treats([4, 5, 6], [1,2,3]) == 0)
