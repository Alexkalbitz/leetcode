# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#


class Solution:
    def lengthOfLongestSubstring(self, s):
        string = ''
        longest = 0
        for n in s:
            if n not in string:
                string += n
            elif n in string:
                if len(string) > longest:
                    longest = len(string)
                string = string.split(n)
                string = string[-1] + n
        if len(string) > longest:
            return len(string)
        else:
            return longest

t = "abcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(t))
