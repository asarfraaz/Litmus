def add(num1, num2):
    return num1 + num2

def usage(prog_name):
    print(f"Usage: {prog_name} num1 num2")
    exit()

def get_numbers(args):
    print(f'{args = }')
    # Check len(args) for
    # python add.py 2
    # x = 2, y = 0

    # Check len(args) for
    # python add.py 2 3
    # x = 2, y = 3

    # Check len(args) for 
    # python add.py
    # print usage and exit

    # Dummy data
    x = y = 0
    return x, y

def main(args):
    x, y = get_numbers(args)
    res = add(x, y)
    print("Result", res)

# Main
if __name__ == "__main__":
    import sys
    main(sys.argv)

