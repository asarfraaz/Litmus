'''
    Inform the user about their final marks
'''

def get_username():
    inp = input("What is your name? ")
    num = input("What is your age? ")
    return inp, num

def get_marks(msg):
    print("Hello", msg)
    marks = input("How much did you score? ")
    return marks

def main():
    name, age = get_username()
    score = get_marks(name)
    # check if score is between 32 and 35
    # then set score to 35
    print(name, age, score)

# Main starts from here
main()
