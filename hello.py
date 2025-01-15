import sys


def hello():
    print("hello")


def ahoj():
    print("ahoj")


def main():
    if sys.argv[1] == "sk":
        ahoj()
    else:
        hello()


if __name__ == "__main__":
    main()
