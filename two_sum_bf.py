# Two Sum
# Brute Force Solution
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            number_to_find = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == number_to_find:
                    return [i, j]
                        