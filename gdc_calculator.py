def gcd_iterative(a, b):
    """
   GDC by using  the iterative Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    """
    GCD by using the recursive Euclidean algorithm.
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
