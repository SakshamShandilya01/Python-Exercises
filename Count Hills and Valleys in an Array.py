
class Solution(object):
    def countHillValley(self, nums):

        arr = []

        for i in nums:
            if len(arr) == 0 or arr[-1] != i:
                arr.append(i)

        count = 0

        for i in range(1, len(arr) - 1):

            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1

            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1

        return count