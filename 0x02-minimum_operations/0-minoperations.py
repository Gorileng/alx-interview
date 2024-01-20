#!/usr/bin/python3
'''The minimum Operations python3 challenge'''


def minOperations(n):
    '''It calculates the fewest number of
    the operations needed to result in exactly the n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, then return 0
    '''
    pasted_chars = 1  # how many chars are in the file
    clipboard = 0  # how many H's are copied
    counter = 0  # the operations counter

    while pasted_chars < n:
        # if it did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment the operations counter
            counter += 1

        # if you haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increments the operations counter
            counter += 1
            # continues the next loop
            continue

        remaining = n - pasted_chars  # remaining characters to Paste
        # checks if is impossible by checking if clipboard
        # have more than needed to reach a number desired
        # which also means that the number of characters in file is equal
        # or more than in a clipboard.
        # in both situations it is impossible to achieve the n of chars
        if remaining < clipboard:
            return 0

        # if it cannot be divided
        if remaining % pasted_chars != 0:
            # pastes the current clipboard
            pasted_chars += clipboard
            # increments the operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increments the operations counter
            counter += 2

    # if you got the desired results
    if pasted_chars == n:
        return counter
    else:
        return 0
