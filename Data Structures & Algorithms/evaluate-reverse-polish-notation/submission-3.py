class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        result_stack = []

        i = 0
        last_string = len(tokens)-1
        while i <= last_string:
            if tokens[i] not in operators:
                result_stack.append(int(tokens[i]))
                i+=1
            else:
                num1 = result_stack.pop()
                num2 = result_stack.pop()
                if tokens[i] == '+':
                    result_stack.append(num1 + num2)
                elif tokens[i] == '-':
                    result_stack.append(num2 - num1)
                elif tokens[i] == '*':
                    result_stack.append(num1 * num2)
                elif tokens[i] == '/':
                    result_stack.append(int(num2 / num1))
                i+=1

        return result_stack[0]
