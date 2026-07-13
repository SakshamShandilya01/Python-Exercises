class Solution(object):
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2

            row = 0

            for i in range(n):
                if mat[i][mid] > mat[row][mid]:
                    row = i

            if mid > 0:
                left = mat[row][mid - 1]
            else:
                left = -1

            if mid < m - 1:
                right = mat[row][mid + 1]

            else:
                right = -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]

            elif left > mat[row][mid]:
                high = mid - 1

            else:
                low = mid + 1



