"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError("Cannot be zero or negative")
    
    list = []
    count=2

    while len(list) < number_of_primes:
            t = True
            for i in range(2, count):
                if count % i == 0:
                    t = False

            if t:
                list.append(count)
            count+=1
    return list
