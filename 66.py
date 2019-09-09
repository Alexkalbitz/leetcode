# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution:
    def plusOne(self, digits):
        index = len(digits)-1
        while index > -1:
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                return digits

        if index == -1:
            digits.insert(0, 1)
            return digits


test = [9, 9, 9, 9]
s = Solution()
print(s.plusOne(test))
