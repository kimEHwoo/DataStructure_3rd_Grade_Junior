# #Logarithmic Function
# def binary_search(sorted_array, target):
#     left, right = 0, len(sorted_array)-1

#     while left <= right:
#         mid = (left + right)//2
#         mid_value = sorted_array[mid]

#         if mid_value == target:
#             return mid
#         elif mid_value < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


# # Linear Function
# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1

# array = [3,5,2,4,9]
# target = 4

# index = linear_search(array, target)

# if index != -1:
#     print(f'Element found at index {index}')
# else:
#     print('Element not found in the array')