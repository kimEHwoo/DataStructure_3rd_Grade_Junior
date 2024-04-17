def isValid(s: str) -> bool:
# -> bool 은 isValid가 bool 형이다라는 것을 주석으로 달아준 것
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack