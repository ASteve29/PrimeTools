import math

def prime_checker(n):
  for i in range(2, math.isqrt(n)):
    if n % i == 0:
      return bool(0)
    else:
      continue
  return bool(1)
