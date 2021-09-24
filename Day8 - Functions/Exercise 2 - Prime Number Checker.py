"""Program to determine whether a number is prime or not"""


def prime_number_checker(n: int) -> bool:
    """Function that return True when n is a prime number, False otherwise"""

    # units = list(range(2, 10))
    # if n in units:
    #     for i in units:
    #         if i == n:
    #             pass
    #         else:
    #             if n % i == 0:
    #                 return False
    #         return True
    # else:
    #     for i in units:
    #         if n % i == 0:
    #             return False
    #         return True

    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


