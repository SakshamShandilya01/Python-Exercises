class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            m = min(nums)
            idx = nums.index(m)
            nums[idx] *= multiplier
        return nums