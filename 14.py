# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs):
        # check for empty list as input
        smallest_prefix = []
        if strs == smallest_prefix:
            return ''
        # sort for the shortest word in the list since the smallest prefix can be the shortest word at max
        strs.sort(key=len)
        for letter in strs[0]:
            smallest_prefix.append(letter)
        # probably should not pop an item from the list but instead just ignore it
        strs.pop(0)
        target_index = 0
        for word in strs:
            for char in range(len(smallest_prefix)):
                # check if the letters match the prefix
                if len(smallest_prefix) == 0:
                    return ''
                if word[char] == smallest_prefix[char]:
                    target_index = char
                # if not cut the prefix
                else:
                    if char is not 0:
                        smallest_prefix = smallest_prefix[: target_index + 1]
                        break
                    else:
                        return ''
        # return whatever is left of the initial prefix as string
        return ''.join(smallest_prefix)


test = ["dogde","dorito","dog"]

s = Solution()
result = s.longestCommonPrefix(test)
print(result)
