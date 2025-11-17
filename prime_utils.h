#ifndef PRIME_UTILS_H
#define PRIME_UTILS_H

#include <cstdint> // Required for int64_t
#include <vector> // Required for std::vector in function declarations

#ifdef __cplusplus
extern "C" {
#endif

// Function declarations (prototypes) with C linkage
extern bool is_prime(int64_t n);
extern int count_primes(int64_t limit);
extern int nth_prime(int64_t n);
extern int previous_prime(int64_t n);
extern int next_prime(int64_t n);
#ifdef __cplusplus
}
#endif

// C++ specific function declaration (no extern "C" needed)
std::vector<int> generate_primes(int64_t limit);
std::vector<int> factor(int64_t n);


#endif // PRIME_UTILS_H
