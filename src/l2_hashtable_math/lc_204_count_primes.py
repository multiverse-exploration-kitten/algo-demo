class Solution:
    def count_primes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of a prime number i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
