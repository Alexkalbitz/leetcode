# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
#
# Example 3:
#
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range: [−231,  231 − 1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        if x < 0:
            is_neg = True
            x *= -1
        else:
            is_neg = False
        new = 0
        while x > 0:
            new = new * 10
            new = new + (x % 10)
            x = x // 10
        if is_neg:
            return new * (-1)
        else:
            return new


numbers = [13, 1221, -25, -121, 5, 222, 1001]
s = Solution()
for n in numbers:
    print(s.reverse(n))
