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



# # find_max
# def find_max(data):
#     max = data[0]
#     for val in data:
#         if val > max:
#             max = val
#     return max


# # O(1)
# def get_first_element(arr):
#     return arr[0] if arr else None #삼항 조건 연산자
# # 만약 arr이 비어있지 않다면 arr[0]을 반환, 그렇지 않으면 None

# # O(n)
# def find_element(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1


# # Quadratic Time Complexity O(n^2)
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr


# compact array
import sys
import array

print(sys.getsizeof(8))
a = 8
print(sys.getsizeof(a))

primes = array.array('i', [2,3,5,7,11])
print(type(primes))
print(primes)

c = "Dog"
print(c)
print(sys.getsizeof(None))