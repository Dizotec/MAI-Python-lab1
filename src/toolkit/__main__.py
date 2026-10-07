import sys
from toolkit import calculator
from toolkit import converter
from toolkit import errors
from toolkit import validation
from toolkit import expression 
def main():
    
    args = sys.argv[1:]  
    if len(args)>=2:
        expression.args = args[1]
    if args[0] == 'calc':
        validation.valid(args)
    
    if args[0] == 'convert':
        converter.convert(args)
if __name__ == "__main__":
    main()
