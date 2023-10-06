import sys
from calculator import calculatore

def main():
    if len(sys.argv) != 4:
        print("Usage: main.py <operation> <num1> <num2>")
    else:
        operation = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])

        result = calculatore(operation, num1, num2)
        print("Result:", result)

if __name__ == "__main__":
    main()
