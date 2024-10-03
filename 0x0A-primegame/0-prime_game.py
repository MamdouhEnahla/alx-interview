#!/usr/bin/python3
"""Prime game module."""

def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes algorithm."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    
    return primes

def count_primes(primes, n):
    """Count the number of primes less than or equal to n."""
    return sum(primes[:n+1])

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    marias_wins = sum(count_primes(primes, n) % 2 for n in nums)
    bens_wins = x - marias_wins
    
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
