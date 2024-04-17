# Sorting a sequence [BubbleSorting]
# Insertion - sort algorithm

# 예) 리스트 A가 [5, 2, 4, 6, 1, 3]
# 먼저, for 루프는 인덱스 1부터 시작하여 리스트의 끝까지 반복합니다.
# 첫 번째 반복에서, cur은 2가 됩니다.
# while 루프는 2가 들어갈 위치를 찾아야 합니다. 
# 이때 j는 1입니다. 
# 현재 A[j-1]은 5이고 5는 2보다 크므로 5를 오른쪽으로 이동시켜야 합니다. 
# 그 결과 리스트는 [5, 5, 4, 6, 1, 3]이 되고, j는 0이 됩니다.
# 그리고 A[0]에는 2가 삽입됩니다.
# 두 번째 반복에서, cur은 4가 됩니다. 
# 그 결과 리스트는 [4, 5, 5, 6, 1, 3]이 되고, j는 1이 됩니다. 그리고 A[1]에는 4가 삽입됩니다.
# 나머지 반복에서도 이와 같은 과정을 반복하여 최종적으로 리스트 A는 [1, 2, 3, 4, 5, 6]으로 정렬됩니다.


def insertion_sort(A):
    '''sort a list of comparable elements into nondecreasing order'''
    for k in range(1, len(A)):      # from 1 to n-1
        cur = A[k]                  # current element to be inserted
        j = k                       # find correct index j for the current
        while j > 0 and A[j-1] > cur: # element A[j-1] must be after the current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

A = [5, 9, 2, 1, 0, 7, 8, 6]
print('Original Sequence:', A)
insertion_sort(A)
print('Sorted Sequence:', A)

B = list('BCDAEHGF')
print('Unsorted Sequence: ', B)
insertion_sort(B)
print('Sorted Sequence: ', B)


print('Initializing 2-D array three wrong way\n')
data = [[0]*3]*3
print(data)
data[2][0] = 5      #[0,0,0]이 동일한 객체를 참조한다
print(data, end = '\n\n')

print('Initializing an array the right way\n')
data2 = [[0]*4 for j in range(3)]
print(data2)
data2[2][0] = 5
data2[0][1] = 2
print(data2)