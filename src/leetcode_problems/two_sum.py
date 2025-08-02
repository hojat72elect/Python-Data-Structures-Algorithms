class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            j_index = index + 1
            while j_index < len(nums):
                if i + nums[j_index] == target:
                    return[index, j_index]
                    break
                j_index += 1