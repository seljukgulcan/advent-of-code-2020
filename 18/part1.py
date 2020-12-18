filename = 'input.txt'

PLUS = 1
MULTIPLY = 2
NOOP = 3

def solve(expr):

    stack = [[0, PLUS]]

    for c in expr:
        if c == ' ':
            continue
        elif c.isdigit():
            rhs = int(c)
            lhs, op = stack[-1]

            if op == PLUS:
                stack[-1][0] = lhs + rhs
            elif op == MULTIPLY:
                stack[-1][0] = lhs * rhs
            else:
                raise ValueError('Unexpected op {}'.format(op))

            stack[-1][1] = NOOP

        elif c == '(':
            stack.append([0, PLUS])
        elif c == ')':
            rhs, op = stack.pop()
            lhs, op = stack[-1]

            if op == PLUS:
                stack[-1][0] = lhs + rhs
            elif op == MULTIPLY:
                stack[-1][0] = lhs * rhs
            else:
                raise ValueError('Unexpected op {}'.format(op))
        elif c == '+':
            stack[-1][1] = PLUS
        elif c == '*':
            stack[-1][1] = MULTIPLY
        else:
            raise ValueError('Unexpected token {}'.format(c))

    return stack[-1][0]


with open(filename) as file:

    answer = 0
    for line in file:
        result = solve(line.strip())
        answer += result
    print(answer)