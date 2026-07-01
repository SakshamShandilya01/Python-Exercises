class Solution(object):
    def sortArray(self, nums):
        self.mergeSort(nums)
        return nums

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1