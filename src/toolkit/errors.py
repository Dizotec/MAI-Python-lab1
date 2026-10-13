import sys


def empty_exp():
        print('Empty Expression', file=sys.stderr)
        sys.exit(2)
def invalid_symbol():
        print('Invalid Symbol', file=sys.stderr)
        sys.exit(2)
def double_operands():
        print('Two Binary Operators in a row', file=sys.stderr)
        sys.exit(2)
def division_by_zero():
        print('Division by zero', file=sys.stderr)
        sys.exit(2)
def missed_operand():
        print('Missing Operand', file=sys.stderr)
        sys.exit(2)
def undefiend_group():
        print("Unknown Unit", file=sys.stderr)
        sys.exit(2)
def conversion_of_different_groups():
        print('Conversion of Different Groups', file=sys.stderr)
        sys.exit(2)
def below_zero():
        print('This Tempreture is not allowed', file=sys.stderr)
        sys.exit(2)
def extra_parenthesis():
        print("Extra parenthesis",file=sys.stderr)
        sys.exit(2)
        