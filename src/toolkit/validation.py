from toolkit import errors 
from toolkit import converter
from toolkit import calculator
from toolkit import tokenization
import sys
def valid(args):
    if len(args) == 1:
            errors.empty_exp()
            sys.exit(2)
    exp_args = args[1]
    
    exp = args[1]

    permitted = ['*','/','-','+','.'] 
    clean_exp = exp.replace(' ', '')
    prev = '+'
    for i in clean_exp:
        if i in permitted and prev in permitted:
            # допустимо только если второй оператор — унарный '+' или '-'
            if not (i in ('+','-') and prev in ('*','/','+','-')):
                errors.double_operands()
        prev = i
    # проверка на пропущенный операнд 
    
    open_bracket_error = ['(' + i for i in permitted] 
    del open_bracket_error[2]
    bracket_error =  open_bracket_error + [ i + ')' for i in permitted] 
    bracket_error_flag = False 
    for i in bracket_error:
        if i in exp:
            bracket_error_flag = True 
    if ( exp[0] == '/' or exp[0] == '*' ) or (exp[-1] in permitted) or bracket_error_flag:
        errors.missed_operand()
        
    for i in range(10):
        permitted.append(str(i))
    # проверка на неподходящие символы 
    permitted.append(')')
    permitted.append('(')
    permitted.append(' ')
    for i in exp:
        if i not in permitted:
            print(i)
            errors.invalid_symbol()
    # проверка на деление на ноль 
    combs_with_div_by_zero = [str(i) +'/0' for i in range(1,10)]
    for i in combs_with_div_by_zero:
        if i in exp:
            errors.division_by_zero()
    
    
    
    tokenization.get_tokens(exp)
