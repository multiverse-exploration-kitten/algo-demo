class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is odd, we can get rid of the middle digit by reverted_number // 10
        return x == reverted_number or x == reverted_number // 10
