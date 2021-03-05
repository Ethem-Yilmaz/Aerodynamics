"""
Dilara Ozev
Ethem Yılmaz
"""

import sys
sys.setrecursionlimit(1000000000)

factorial = lambda num: 1 if num<=1 else factorial(num-1)*num
factorial.__doc__= f"Returns the factorial of given number. (Up to 1000000000)"

combination = lambda num,el=0: int(factorial(num)/(factorial(el)*factorial(num-el)))
combination.__doc__= "Takes 2 parameters number and element. Returns 'element' combination of 'number'"

def fibonacci(index):
    """
    \n \n \n
    Parameters
    ----------
    index : Index of the number wanted in fibonacci series

    Returns
    -------
    Indexed Numbers

    """
    start = 1
    fibonacci = [1]
    for i in range(1,index+1):
        fibonacci.append(start)
        start = fibonacci[i]+fibonacci[i-1]
    
    return fibonacci[index-1]

def prime_numbers(number=3):
    """
    

    Parameters
    ----------
    number : Upper bound of numbers

    Returns
    -------
    primes : List of Prime Numbers up to given number. First element is two

    """
    primes = [2]
    for i in range(3, number+1,2):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes