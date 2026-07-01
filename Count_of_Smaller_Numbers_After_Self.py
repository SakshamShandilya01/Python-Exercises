class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        self.count = [0] * n

        arr = [(nums[i], i) for i in range(n)]

        self.mergeSort(arr)

        return self.count

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        merged = []

        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                self.count[left[i][1]] += j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            self.count[left[i][1]] += j
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged