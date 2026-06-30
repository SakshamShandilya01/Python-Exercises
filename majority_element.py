class Solution(object):
    def majorityElement(self, nums):

        count = {}

        for i in range(len(nums)):

            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1

        for key in count:

            if count[key] > len(nums) // 2:
                return key