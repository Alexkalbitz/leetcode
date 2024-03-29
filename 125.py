# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
#
# Input: "race a car"
# Output: false


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-z]+', '', s)
        for i in range(len(s)//2):
            if s[i] == s[-(i+1)]:
                continue
            else:
                return False
        return True


test = 'abcdccba'
s = Solution()
print(s.isPalindrome(test))
