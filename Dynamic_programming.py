
import sys


def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def dynamic_fibonacci(n, memo={}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]

    except KeyError:
        result = dynamic_fibonacci(n - 1, memo) + dynamic_fibonacci(n - 2, memo)
        memo[n] = result

        return result


def main():

    sys.setrecursionlimit(10000)
    n = int(input("Select a number: "))
    result = dynamic_fibonacci(n)
    print(result)


if __name__ == "__main__":
    main()
