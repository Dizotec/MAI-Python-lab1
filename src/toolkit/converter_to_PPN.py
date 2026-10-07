from collections import deque 
from toolkit import calculator
def isfloat(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
    
def convert_to_RPN(tokens):
    
    converted = []
    stack = deque()
    priorities = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2,'~':3}
    for i in tokens:
    
        if i == ' ':
            continue 
        if i.isdigit() or isfloat(i):
            converted.append(i)
        elif i == '(':
            stack.append(i)
        elif i in "+-/*~":
            while stack and stack[-1] != '(' and priorities[stack[-1]] >= priorities[i]:
                converted.append(stack.pop())
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] != '(':
                converted.append(stack.pop())
            stack.pop()
    while stack:
        converted.append(stack.pop())
   
    calculator.calc(converted)

