class Solution:
    def divideArray(self, nums):
        count = {}

        # Count how many times each number appears
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        # Check if every number appears an even number of times
        for num in count:
            if count[num] % 2 != 0:
                return False

        return True