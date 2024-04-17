import pdb
def evalRPN(tokens):
    stack = []
    operators = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y,
                 "/": lambda x, y: int(x / y)}
    
    for token in tokens:
        if token in operators:
            y = stack.pop()
            x = stack.pop()
            #pdb.set_trace()
            operation = operators[token]
            result = operation(x, y)
            stack.append(result)
        
        else:
            stack.append(int(token))

    return stack[-1]

rpn_expression = ["1", "5", "3", "-","8", "-","2" , "+","+" ]


print(evalRPN(rpn_expression))