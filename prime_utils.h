#ifndef PRIME_UTILS_H
#define PRIME_UTILS_H

#include <vector> // Required for std::vector in function declarations

#ifdef __cplusplus
extern "C" {
#endif

// Function declarations (prototypes) with C linkage
extern bool is_prime(int n);
extern int count_primes(int limit);
extern int nth_prime(int n);
extern int previous_prime(int n);
extern int next_prime(int n);

#ifdef __cplusplus
}
#endif

// C++ specific function declaration (no extern "C" needed)
std::vector<int> generate_primes(int limit);
std::vector<int> factor(int n);


#endif // PRIME_UTILS_H
