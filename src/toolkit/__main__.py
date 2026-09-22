import sys
from toolkit import calculator
from toolkit import converter
from toolkit import errors
from toolkit import validation
def main():
    
    args = sys.argv[1:]  
    print(f"Переданные аргументы: {args}")
    validation.valid(args)

if __name__ == "__main__":
    main()
