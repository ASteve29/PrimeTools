import math

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
      return False
    else:
      continue
  return True

def count_primes_up_to(limit):
  count = 0
  for num in range(2, limit + 1):
    if is_prime(num):
      count += 1
  return count

def generate_primes_up_to(limit):
  primes = []
  if limit < 2:
    raise ValueError("limit must be at least 2 to generate primes.")
  for i in range(2, limit):
    if is_prime(i):
      primes.append(i)
  return primes

def nth_prime(n):
  if n <= 0:
    raise ValueError("n must be greater than 0 to find a prime.")
  count = 0
  num = 1
  while True:
    num += 1
    if is_prime(num):
      count += 1
      if count == n:
        return num

def factor(n):
    if n < 2:
        raise ValueError("n must be greater than 1 to factor.")
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

def previous_prime(n):
    if n <= 2:
        raise ValueError("No prime exists before 2.")
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i

def next_prime(n):
  num = n + 1
  if n <= 0:
    raise ValueError("n must be greater than 0 to find the next prime.")
  while not is_prime(num):
    num = num + 1
  return num
