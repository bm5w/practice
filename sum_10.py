"""Function that returns first two numbers that sum to 10, from a list."""


def sum10(in_ls):
    for x in in_ls:
        for y in in_ls:
            if x + y == 10:
                return x, y
