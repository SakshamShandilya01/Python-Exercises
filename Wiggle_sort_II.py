class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        n = len(nums)

        mid = (n - 1) // 2

        left = nums[:mid + 1]
        right = nums[mid + 1:]

        i = len(left) - 1
        j = len(right) - 1

        k = 0

        while i >= 0:
            nums[k] = left[i]
            i -= 1
            k += 2

        k = 1

        while j >= 0:
            nums[k] = right[j]
            j -= 1
            k += 2