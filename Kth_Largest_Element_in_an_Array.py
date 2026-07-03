class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()

        n = len(nums)

        return nums[n - k]