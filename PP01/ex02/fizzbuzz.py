import sys

def fizzBuzz():
    args = sys.argv

    if len(args) != 2:
            sys.exit()

    for i in range(1, int(args[1]) + 1):
        if ((i % 15 == 0)):
            print("fizzbuzz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0):
            print("fizz")
        else:
            print(i)

if __name__ == '__main__':
    fizzBuzz()
