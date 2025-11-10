#include "prime_utils.h" // Assuming this file exists and contains function declarations
#include <cmath>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

extern "C" bool is_prime(int n){
    if(n < 2){
        return false;
    }
    // Optimized loop condition to use std::sqrt and run more efficiently
    for(int i = 2; i * i <= n; i ++){ 
        if(n % i == 0){
            return false;
        }
        // 'else { continue; }' is redundant and removed
    }
    return true;
}

extern "C" int count_primes(int limit){
    int count = 0;
    for(int i = 2; i < limit; i++){
        if(is_prime(i)){
            count++;
        }
    }
    return count;
}

std::vector<int> generate_primes(int limit){
    std::vector<int> primes;
    if(limit < 2){
        return primes;
    }
    primes.push_back(2);
    for (int i = 3; i <= limit; i += 2) {
        bool is_prime = true;
        int max_divisor = static_cast<int>(std::sqrt(i)); 
        for (int j = 3; j <= max_divisor; j += 2) {
            if (i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            primes.push_back(i); 
        }
    }
    return primes;
}

extern "C" int nth_prime(int n){
    if (n <= 0) return -1;
    int count = 0;
    for(int i = 2; count != n; i++){
        if(is_prime(i)){
            count++;
        }
        if(count == n){
            return i;
        }
    }
    return -1;
}

std::vector<int> factor(int n){
    std::vector<int> factors;
    if(n < 2){
        return factors;
    }
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}

extern "C" int previous_prime(int n){
    if(n <= 2){
        return -1;
    }
    for(int i = n - 1; i >= 2; i--){
        if(is_prime(i)){
            return i;
        }
    }
    return -1;
}

extern "C" int next_prime(int n){
    for(int i = n + 1; ; i++){
        if(is_prime(i)){
            return i;
        }
    }
}
