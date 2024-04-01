def is_balanced(expression):
    # Initialize an empty stack
    stack = []

    # Mapping of closing to opening parentheses
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)  # Push the opening parentheses onto the stack
        elif char in mapping.keys():
            if stack and stack[-1] == mapping[char]:
                stack.pop()  # Pop the matching opening parentheses
            else:
                return False  # Unmatched closing parenthesis

    return not stack  # If stack is empty, parentheses are balanced

# Test the function
print("Is '(a + b) * (c + d)' balanced?", is_balanced('(a + b) * (c + d)'))
print("Is '(a + b) * (c + d]' balanced?", is_balanced('(a + b) * (c + d]'))
