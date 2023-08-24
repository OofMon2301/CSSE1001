def is_prime(n):
    """Returns True iff 'n' is prime.

    Parameters:
        n (int): Integer value to be tested to see if it is prime.

    Return:
        bool: True if 'n' is prime. False otherwise.

    Preconditions:
        n > 1
    """
    for i in range(2, n):
        # Check if i is prime
        if n % i == 0:
            return False
    return True


def get_primes(n):
    """Return a list of the first n primes.

    Parameters:
        n (int): Number of prime numbers to find.

    Return:
        list[int]: The first 'n' prime numbers.

    Preconditions:
        n > 0
    """
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i) is True:
            primes.append(i)
        else:
            pass
        i += 1
    return primes


n = int(input("How many primes? "))
print("The first " + str(n) + " primes are: ", get_primes(n))
