"""
Searches for a certain word in a text file.
"""

import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help="Specify the word to search for")
    parser.add_argument("fname", help="The relative path to file")
    args = parser.parse_args()

    search_file = open(args.fname)
    line_num, found = 0, False

    for line in search_file.readlines():
        line = line.strip('\n\r')
        line_num += 1
        search_result = re.search(args.word, line, re.M | re.I)
        if search_result:
            print(args.word, " Found on line ", line_num)
            found = True
            
    if not found:
        print(args.word, " Not Found")


if __name__ == "__main__":
    main()
