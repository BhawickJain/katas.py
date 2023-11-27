import sympy

print(list(sympy.primerange(0, 100)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
The prime factors of 13195 are 5, 7, 13 and 29.
acti
What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(n):
  list_primes = list(sympy.primerange(0, n))
  prime_factors = []
  result = n

  while result != 1:

    # go through a list of primes, to find the first prime that divides
    for prime in list_primes:
      if result % prime == 0:
        # save result and keep the prime
        prime_factors.append(prime)
        result = result / prime
        # break from the for loop
        break

  print(prime_factors)
  print(prime_factors[-1])
  print('finished')


largest_prime_factor(13195)
largest_prime_factor(12)
largest_prime_factor(600851475143)