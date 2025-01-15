import sys


def hello():
    print("hello")


def ahoj():
    print("ahoj")


def bonjour():
    print("bonjour")


def main():
    if sys.argv[1] == "sk":
        ahoj()
    elif sys.argv[1] == "fr":
        bonjour()
    else:
        hello()


if __name__ == "__main__":
    main()
