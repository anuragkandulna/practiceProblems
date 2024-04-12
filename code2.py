# PROBLEM STATEMENT 2:
# Given a string verify that a permutation of the characters is a palindrome or not.
# Tc 1: input = "abc" | output = False
# Tc 2: input = "aba" | output = True
# Tc 3: input = "aa" | output = True
# Tc 4: input = "" | output = print error [Here assumption is that null strings are invalid inputs]


def isPalindrome(inputStr):
    """Return True/False if valid palindrome string. Else return None."""

    if len(inputStr) <= 0:
        print('Null string given as input.')
        return

    hashMap = {}
    for c in inputStr:
        hashMap[c] = hashMap.get(c, 0) + 1

    # Logic is that if the string is palindrome then the number of characters with odd numbers is either 0 or 1.
    # i.e, the middle index can have only 1 char if length is odd, but in case of odd its 0
    oddCharCount = 0
    for k, v in hashMap.items():
        if v % 2 != 0:
            oddCharCount += 1

    return oddCharCount <= 1


# Test cases
testCases = ["abc", "aba", "aa", ""]

for s in testCases:
    print(isPalindrome(inputStr=s))
