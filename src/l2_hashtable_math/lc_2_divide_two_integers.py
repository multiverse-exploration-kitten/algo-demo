class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Check if the result should be positive or negative
        is_positive = (dividend < 0) == (divisor < 0)

        # If the dividend is the smallest possible number and the divisor is -1,
        # the result would be too big, so we return the biggest possible number
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # Make both numbers positive
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        max_int = 2**31 - 1

        # These lists will keep track of multiples of the divisor
        doubles = []
        power_of_two = []
        n = 1

        # Keep doubling the divisor and store the results
        while dividend >= divisor:
            doubles.append(divisor)
            power_of_two.append(n)

            divisor += divisor
            n += n

        res = 0

        # Subtract the largest possible multiples of the divisor from the dividend
        for idx, d in enumerate(reversed(doubles)):
            if d > dividend:
                continue

            res += power_of_two[len(power_of_two) - 1 - idx]
            dividend -= d

        # If the result should be positive, return the result
        if is_positive:
            return res

        # If the result should be negative, return the negative result
        return -res
