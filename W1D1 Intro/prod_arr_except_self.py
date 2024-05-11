# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# naive solution:
# initialize result arr
# iterate over array
# - get product of all elements that are not current element (2 array slices)
# - append product to result
# return result

# refine:
# create array containing products of all values to the left of the given index
# create array containing products of all values to the right of the given index
# create array containing (left * right) for each index and return

# on review with team:
# a more efficient solution: instead of creating two arrays, one for right and one for left, just create the one for left, and then write to your result array as you iterate from right to left and calculate the right product; this improves the space complexity and also takes away the need to reverse the right_products array before making the final calculation (though I could have used two pointers for that instead).

def productExceptSelf(nums):
    left_products = []
    right_products = []

    running_product = 1
    for idx in range(0, len(nums)):
        left_products.append(running_product)
        running_product *= nums[idx]

    running_product = 1
    for idx in range(len(nums) - 1, -1, -1):
        right_products.append(running_product)
        running_product *= nums[idx]

    right_products.reverse()

    return [left_products[idx] * right_products[idx] for idx in range(0, len(nums))]

nums = [1,2,3,4]
print(productExceptSelf(nums) == [24,12,8,6])

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums) == [0,0,9,0,0])
