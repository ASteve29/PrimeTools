from libcpp.vector cimport vector
from libc.stdint cimport int64_t

# --- C++ functions ---
cdef extern from "prime_utils.h":
    bint is_prime(int64_t n)
    int64_t count_primes(int64_t limit)
    int64_t nth_prime(int64_t n)
    int64_t previous_prime(int64_t n)
    int64_t next_prime(int64_t n)
    vector[int64_t] generate_primes(int64_t limit)
    vector[int64_t] factor(int64_t n)

# --- Python wrappers ---
def py_is_prime(n):
    return is_prime(<int64_t>n)

def py_count_primes(n):
    return count_primes(<int64_t>n)

def py_nth_prime(n):
    return nth_prime(<int64_t>n)

def py_previous_prime(n):
    return previous_prime(<int64_t>n)

def py_next_prime(n):
    return next_prime(<int64_t>n)

def py_generate_primes(n):
    cdef vector[int64_t] v = generate_primes(<int64_t>n)
    return list(v)

def py_factor(n):
    cdef vector[int64_t] v = factor(<int64_t>n)
    return list(v)
