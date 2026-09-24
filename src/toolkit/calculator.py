from collections import deque 
from toolkit import errors
from toolkit import converter_to_PPN

def calc(converted):
    stack = deque() 
    
    for i in converted:
        if i =='~':
            arg = float(stack.pop())
            stack.append(str(-arg))
        elif i.isdigit() or converter_to_PPN.isfloat(i):
            stack.append(i)
        elif i in '+-/*':
            f_arg = float(stack.pop())
            s_arg = float(stack.pop())
            if i == '+':
                stack.append(str(s_arg+f_arg))
            elif i == '*':
                stack.append(str(s_arg*f_arg))
            elif i == '/':
                if f_arg == 0:
                    errors.division_by_zero()
                stack.append(str(s_arg/f_arg))
            elif i == '-':
                stack.append(str(s_arg-f_arg))
    print(stack[0])

    
