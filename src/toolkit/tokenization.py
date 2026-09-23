from toolkit import converter_to_PPN
def get_tokens(exp):
    
    
    tokens = [] 
    i = 0 
    while i < len(exp):
        if exp[i] in '+-/*()':
            tokens.append(exp[i])
            i+=1
        elif exp[i].isdigit() or exp[i] == '.':
            number = ""
            while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
                number += exp[i]
                i += 1
            tokens.append(number)
    
    converter_to_PPN.convert_to_RPN(tokens)
