"""Convert a decimal number to binary representation.

For example, using our solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""

# HOW TO CONVERT: keep dividing by two until quotient is 1. Within
# each divide, remainder (always either 0 or 1) is the binary # to be added.
# result should be last append to first append


def dec2bin_forwards(num):
    """Convert a decimal number to binary representation."""

    # convert num to binary, then convert into lst
    binary_num = str(bin(num))

    binary_lst = []

    for char in binary_num:
        binary_lst.append(char)

    result = []

    # create new lst of binary digits after 'b' appears
    for i, char in enumerate(binary_num):
        if char == 'b':
            result.append(binary_num[i + 1:])

    result = "".join(result)

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
