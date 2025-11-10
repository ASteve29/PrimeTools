# prime_wrapper.pyx
# distutils: language = c++

from libcpp.vector cimport vector

# --- C-linkage functions ---
cdef extern from "prime_utils.h":
    bint is_prime(int n)          # match exactly the header
    int count_primes(int limit)
    int nth_prime(int n)
    int previous_prime(int n)
    int next_prime(int n)

# --- C++ only functions ---
cdef extern from "prime_utils.h":
    vector[int] generate_primes(int limit)
    vector[int] factor(int n)

# --- Python wrappers ---
def py_is_prime(int n):
    return is_prime(n)

def py_count_primes(int limit):
    return count_primes(limit)

def py_nth_prime(int n):
    return nth_prime(n)

def py_previous_prime(int n):
    return previous_prime(n)

def py_next_prime(int n):
    return next_prime(n)

def py_generate_primes(int limit):
    cdef vector[int] v = generate_primes(limit)
    return list(v)

def py_factor(int n):
    cdef vector[int] v = factor(n)
    return list(v)
