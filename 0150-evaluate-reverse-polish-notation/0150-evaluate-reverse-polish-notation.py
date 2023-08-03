class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(a / b)
        }
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                operation = operations[token]
                stack.append(operation(num2, num1))
        return stack.pop()
