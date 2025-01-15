import sys


def hello():
    print("hello")


def bonjour():
    print("bonjour")


def main():
    if sys.argv[1] == "fr":
        bonjour()
    else:
        hello()


if __name__ == "__main__":
    main()
