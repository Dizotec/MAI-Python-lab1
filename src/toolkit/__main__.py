import sys
from toolkit import calculator
from toolkit import converter
from toolkit import errors
from toolkit import validation
from toolkit import expression 
def main():

    args = sys.argv[1:]  
    if '-help' in args or not args:
        print("Usage guide:\n  python -m toolkit calc \"expression\"\n  python -m toolkit convert VALUE --from UNIT --to UNIT")
        sys.exit(0)
    if len(args)>=2:
        expression.args = args[1]
    if args[0] == 'calc':
        res = validation.valid(args)
        print(res)
    
    if args[0] == 'convert':
        res = converter.convert(args)
        print(res)
if __name__ == "__main__":
    main()
