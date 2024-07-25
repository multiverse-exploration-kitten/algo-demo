class Solution:
    def my_pow(self, x: float, n: int) -> float:
        # Start with the result as 1, because any number to the power of 0 is 1
        res = 1

        # If n is negative, convert n to positive and take the reciprocal of x
        if n < 0:
            n = -n  # Make n positive
            x = 1 / x  # Take the reciprocal of x

        # Loop until n becomes 0
        while n > 0:
            # If n is even
            if n % 2 == 0:
                x = x * x  # Square the base
                n = n // 2  # Divide n by 2

            # If n is odd
            else:
                res = res * x  # Multiply result by x
                n -= 1  # Subtract 1 from n to make it even
                x = x * x  # Square the base again
                n = n // 2  # Divide n by 2

        # Return the final result
        return res
