def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
nums = [2, 1, 2, 4, 3]
print(nextGreaterElement(nums))

# 2 다음으로 큰 요소는 4입니다.
# 1 다음으로 큰 요소는 2입니다.
# 2 다음으로 큰 요소는 4입니다.
# 4 다음으로 큰 요소는 없으므로 -1입니다.
# 3 다음으로 큰 요소는 없으므로 -1입니다.
# [4, 2, 4, -1, -1]