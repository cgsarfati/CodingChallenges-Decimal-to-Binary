"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

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


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    # HOW TO CONVERT: keep dividing by two until quotient is 1. Within
    # each divide, remainder (always either 0 or 1) is the binary # to be added.

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
