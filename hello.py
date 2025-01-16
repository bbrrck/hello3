import sys


def hello():
    print("hello!!")


def ahoj():
    print("ahoj!!")


def bonjour():
    print("bonjour!!")


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
