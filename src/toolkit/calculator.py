from collections import deque 

from toolkit import errors
from toolkit import validation
    
from toolkit import expression
from toolkit import converter_to_PPN
from decimal import Decimal,  ROUND_HALF_UP
import json 
def calc(converted):
    stack = deque() 
    for i in converted:
        if i =='~':
            arg = float(stack.pop())
            stack.append(str(-arg))
        elif i.isdigit() or converter_to_PPN.isfloat(i):
            stack.append(i)
        elif i in '+-/*':
            try:
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
            except IndexError:
                errors.missed_operand()
    value = Decimal(stack[0])
    result = str(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)) # rounding to 2 decimal places
    expression_plus_result = expression.args +  '=' + result
    
    with open('results.json','a',encoding='utf-8') as file:
        json.dump(expression_plus_result,file)
        file.write('\n')
    return expression_plus_result
   

    
