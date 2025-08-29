import math

def prime_checker(n):
  for i in range(2, sqrt(n)):
    if n % i == 0:
      return false
    else:
      continue
  return true
