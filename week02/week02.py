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


# # compact array
# import sys
# import array

# print(sys.getsizeof(8))
# a = 8
# print(sys.getsizeof(a))

# primes = array.array('i', [2,3,5,7,11])
# print(type(primes))
# print(primes)

# 'b': 부호 있는 정수 (signed char)
# array.array('b', [-1, 0, 1, 2, 3])
# 'B': 부호 없는 정수 (unsigned char)
# array.array('B', [0, 1, 2, 3, 4])
# 'h': 부호 있는 정수 (signed short)
# array.array('h', [-32768, 0, 32767])
# 'H': 부호 없는 정수 (unsigned short)
# array.array('H', [0, 1, 2, 3, 4, 65535])
# 'i': 부호 있는 정수 (signed int)
# array.array('i', [-2147483648, 0, 2147483647])
# 'I': 부호 없는 정수 (unsigned int)
# array.array('I', [0, 1, 2, 3, 4, 4294967295])
# 'f': 부동 소수점 수 (float)
# array.array('f', [0.1, 0.2, 0.3, 0.4, 0.5])
# 'd': 부동 소수점 수 (double)
# array.array('d', [0.1, 0.2, 0.3, 0.4, 0.5])

# c = "Dog"
# print(c)
# print(sys.getsizeof(None))


# #analyzing a dynamic array
# import sys
# data = []
# for k in range (27):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
#     data.append(None)



# # Implementing a dynamic array
# import ctypes
# class DynamicArray:
#   ''' A dynamic array class akin to a simplified Python list '''
#   def __init__(self):
#     ''' create an empty array '''
#     self._n = 0                                 # count actual elements
#     self._capacity = 1                          # default array capacity
#     self._A = self._make_array(self._capacity)  # low-level array

#   def __len__(self):
#     ''' return number of elements stored in the array'''
#     return self._n

#   def __getitem__(self, k):
#     ''' return element at index k '''
#     if not 0 <= k < self._n:
#       raise IndexError('invalid index')
#     return self._A[k]

#   def append(self, obj):
#     ''' Add object to the end of the array'''
#     if self._n == self._capacity:  # no enough room
#       self._resize(2*self._capacity) # so double the capacity
#     self._A[self._n] = obj
#     self._n += 1

#   def _resize(self, c):
#     ''' Resize the internal array to capacity c'''
#     B = self._make_array(c)       # new (bigger) array
#     for k in range(self._n):
#       B[k] = self._A[k]           # copy data from old array into new array
#     self._A = B                   # use the bigger array
#     self._capacity = c


#   def _make_array(self, c):    # nonpublic utility
#     ''' Return new array with capacity c'''
#     return (c * ctypes.py_object)()


#   def insert(self, k, value):
#     '''
#     Insert value at index k, shifting subsequent values rightward
#     For simplicity, we assume 0 <= k <= n
#     '''
#     if not 0 <= k <= self._n:
#       raise ValueError("k must lie between 0 and n.")

#     if self._n == self._capacity:
#       self._resize(2*self._capacity)
#     for j in range(self._n, k,-1):  # shift rightmost first
#       self._A[j] = self._A[j-1]
#     self._A[k] = value
#     self._n += 1

#   def remove(self, value):
#     '''
#     Remove first occurrence of value (or raise ValueError)
#     note: We do not consider shrinking of dynamic array in
#     this  version
#     '''
#     for k in range(self._n):
#       if self._A[k] == value: # found a match
#         for j in range(k, self._n-1): # shift others to fill gap
#           self._A[j] = self._A[j+1]
#         self._A[self._n-1] = None   # help garbage collection
#         self._n -= 1 # We have now one less item
#         return       # exit if match found
#     raise ValueError('value not found') #only reached if no match

#   def __str__(self):
#     '''
#     Getting a string representation of the array
#     '''
#     string = str()
#     for i in range(0, self._n):
#       string = string + str(self._A[i]) +', '
#     return '< ' + string + ' >'



# # timeit_append
# import timeit

# def append_test():
#     lst = []
#     for i in range(1000000):
#         lst.append(i)

# time_taken = timeit.timeit(append_test, number = 1)
# print(f"Time taken to append 1,000,000 items: {time_taken} seconds")



# # Amortized Behaviour
# # Append method
# from time import time
# def compute_average(n):
#     data = []
#     start = time()
#     for k in range(n):
#         data.append(None)
#     end = time()
#     return (end-start)/n
# print("Average time per second = {}".format(compute_average(100)))
# print("Average time per operation={}".format(compute_average(1000)))
# print("Average time per operation={}".format(compute_average(10000)))
# print("Average time per operation={}".format(compute_average(100000)))
# print("Average time per operation={}".format(compute_average(1000000)))
# print("Average time per operation={}".format(compute_average(100000000)))

# B = DynamicArray()
# B.append(1)
# B.append(5)
# B.append(7)
# print("Array Length: {}".format(len(B)))
# print(B)
# B.insert(2, 10)
# print(B)
# print("Array Length: {}".format(len(B)))
# B.insert(3, -10)
# print(B)
      


# # time for Inserting element
# from time import time

# def compute_average_insert1(n):
#     '''insert element at the beginning of the list'''
#     data = []
#     start = time()
#     for k in range(n):
#         data.insert(0, None)
#     end = time()
#     return (end-start)/k

# def compute_average_insert2(n):
#     '''insert element at the half of the list'''
#     data = []
#     start = time()
#     for k in range(n):
#         data.insert(n//2, None)
#     end = time()
#     return (end-start)/k

# def compute_average_insert3(n):
#     '''insert element at the end of the list'''
#     data = []
#     start = time()
#     for k in range(n):
#         data.insert(n, None)
#     end = time()
#     return (end-start)/k

# print("Average time per operation={}".format(compute_average_insert1(100)))
# print("Average time per operation={}".format(compute_average_insert2(1000)))
# print("Average time per operation={}".format(compute_average_insert3(10000)))
# print("Average time per operation={}".format(compute_average_insert1(100000)))
# print("Average time per operation={}".format(compute_average_insert2(1000000)))



# C = DynamicArray()
# C.append(1)
# C.append(5)
# C.append(7)
# print(C)
# print("Array Length:{}".format(len(C)))
# C.remove(5)
# print(C)
# print("New Array Length:{}".format(len(C)))


# import time

# n = 100000
# start_time = time.time()
# squares = [k * k for k in range(1, n + 1)]
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"소요 시간: {elapsed_time:.7f} 초")

# st = time.time()
# document = 'Datastr12345uctures'
# letters= ''
# for c in document:
#     if c.isalpha():
#         letters +=c
# en = time.time()
# print(f"time to take {en-st:0.7}")
# print(letters)