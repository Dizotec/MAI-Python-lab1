from collections import deque 
import sys
from toolkit import converter_to_PPN

def calc(converted):
    stack = deque() 
    for i in converted:
        if i.isdigit() or converter_to_PPN.isfloat(i):
            stack.append(i)
        if i in '+-/*':
            f_arg = float(stack.pop())
            s_arg = float(stack.pop())
            if i == '+':
                stack.append((f_arg+s_arg))
            elif i == '*':
                stack.append(str(f_arg*s_arg))
            elif i == '/':
                stack.append(str(f_arg/s_arg))
            elif i == '-':
                stack.append(str(f_arg-s_arg))
    print(stack[0])

    
