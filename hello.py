import sys


def hello():
    # this is a test
    print("hello!!!")


def ahoj():
    # another test
    print("ahoj!!!")


def bonjour():
    print("bonjour!!!")


def main():
    # this code is awesome
    if sys.argv[1] == "fr":
        bonjour()
    elif sys.argv[1] == "sk":
        ahoj()
    else:
        hello()


if __name__ == "__main__":
    main()
