from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                # int로의 변환을 시도하여 숫자인지 판별합니다.
                stack.append(int(token))
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                elif token == "/":
                    result = math.trunc(num2 / num1)  # 정수 나눗셈의 결과를 얻습니다.
                stack.append(result)
        return stack.pop()