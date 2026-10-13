import sys


def empty_exp() -> None:
    print('Empty Expression', file=sys.stderr)
    sys.exit(2)

def invalid_symbol() -> None:
    print('Invalid Symbol', file=sys.stderr)
    sys.exit(2)

def double_operands() -> None:
    print('Two Binary Operators in a row', file=sys.stderr)
    sys.exit(2)

def division_by_zero() -> None:
    print('Division by zero', file=sys.stderr)
    sys.exit(2)

def missed_operand() -> None:
    print('Missing Operand', file=sys.stderr)
    sys.exit(2)

def undefiend_group() -> None:
    print("Unknown Unit", file=sys.stderr)
    sys.exit(2)

def conversion_of_different_groups() -> None:
    print('Conversion of Different Groups', file=sys.stderr)
    sys.exit(2)

def below_zero() -> None:
    print('This Tempreture is not allowed', file=sys.stderr)
    sys.exit(2)
def extra_parenthesis() -> None:
    print("Extra parenthesis", file=sys.stderr)
    sys.exit(2)
