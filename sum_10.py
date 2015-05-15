"""Function that returns first two numbers that sum to 10, from a list."""


def sum10(in_ls):
    # """double for loop implementations."""
    # for x in in_ls:
    #     for y in in_ls:
    #         if x + y == 10:
    #             return x, y

    """Additional memory implementation."""
    foo = []
    for x in in_ls:
        temp = 10-x
        if temp in foo:
            return temp, x
        else:
            foo.append(temp)
