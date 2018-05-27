"""
Match - Checks if the whole string matches the pattern
Search - Searches for the pattern in the string

Option Flags
re.I : Ignore case matching
re.M : Make $ match at the end of a line and ^ at the start of the line
re.S : Makes .(dot). Match any character even the new line character
re.U : Interprets in unicode
re.X : Ignores the whitespace within the pattern

Search and replace done with sub (substitute)

"""

import re

def main():
    line = "I think I understand regular expressions"

    # re.I - case insensitive
    match_result = re.match("think", line, re.M | re.I)
    if match_result:
        print ("Match found", match_result.group())
    else:
        print ("No Match was found")

    search_result = re.search("think", line, re.M|re.I)
    if search_result:
        print ("Search found ", search_result.group())
    else:
        print ("No search found")

if __name__ == "__main__":
    main()