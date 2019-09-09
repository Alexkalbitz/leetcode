# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    def jump(self, nums):
        distance = len(nums)-1
        if distance == 0:
            return 0
        max_jump = nums[0]
        current_index = 0
        finish_index = distance
        number_of_jumps = 0
        while current_index < finish_index:
            if current_index + nums[current_index] >= distance:
                return number_of_jumps + 1
            best = 0
            for x in range(current_index + 1, max_jump + current_index + 1):
                reach = nums[x] + x
                if reach == 0:
                    pass
                elif reach > best:
                    best = reach
                    best_index = x
            max_jump = nums[best_index]
            current_index = best_index
            number_of_jumps += 1



test = [1,2,1,2,2,0,1,5,1,1,0,3,1,1]
s = Solution()
print(s.jump(test))
