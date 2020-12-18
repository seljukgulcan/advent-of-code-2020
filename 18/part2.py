filename = 'input.txt'

PLUS = 1
MULTIPLY = 2
NOOP = 3


def solve(expr):

    factors = [1]
    mode = MULTIPLY

    i = 0
    while i < len(expr):
        c = expr[i]
        if c == ' ':
            i += 1
            continue
        elif c.isdigit():
            no = int(c)
            if mode == PLUS:
                factors[-1] = factors[-1] + no
            else:
                factors.append(no)

        elif c == '(':

            parenthesis_count = 1
            i = i + 1
            start = i
            while i < len(expr):
                c = expr[i]

                if c == ')':
                    parenthesis_count -= 1
                    if parenthesis_count == 0:
                        break
                elif c == '(':
                    parenthesis_count += 1

                i += 1
            end = i

            parenthesis = expr[start:end]

            no = solve(parenthesis)

            if mode == PLUS:
                factors[-1] = factors[-1] + no
            else:
                factors.append(no)
        elif c == '+':
            mode = PLUS
        elif c == '*':
            mode = MULTIPLY
        else:
            raise ValueError('Unexpected token {}'.format(c))

        i += 1

    retval = 1
    for factor in factors:
        retval *= factor
    return retval


with open(filename) as file:

    answer = 0
    for line in file:
        result = solve(line.strip())

        answer += result
    print(answer)
