#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        sys.stderr.write('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        sys.exit(1)
    op = sys.argv[2]
    if op not in '+-*/':
        error = 'Unknown operator. Available operators: +, -, * and /\n'
        sys.stderr.write(error)
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, op, b, result))
