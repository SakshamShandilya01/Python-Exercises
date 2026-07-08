class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)

        return ans