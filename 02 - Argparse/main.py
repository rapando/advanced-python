"""
Argparse

- Positional arguments are required and do not require a -
- optional arguments are preceded with a (-)
- Mutually exclusive options are those that only one can be chosen at once
    like verbose and quiet

"""
import argparse


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    # group is used to add mutually exclusive arguments
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    parser.add_argument('num',
                        help="The fibonacci number you wish to calculate",
                        type=int)
    parser.add_argument('-o', '--output', help='Output result to a file',
                        action='store_true')

    args = parser.parse_args()

    result = fibo(args.num)

    if args.verbose:
        print("Fib ", args.num, " is ", result)
    elif args.quiet:
        print(result)
    else:
        print("Fib(", args.num, ") = ", result)

    if args.output:
        f = open('file.txt', 'a')
        f.write(str(args.num) + "," + str(result) + '\n')


if __name__ == "__main__":
    main()
