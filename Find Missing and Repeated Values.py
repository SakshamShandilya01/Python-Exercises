class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        n=len(grid)
        d=m=0
        counts = {}
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                counts[val] = counts.get(val, 0) + 1
        for num in range(1,n*n+1):
            c = counts.get(num, 0)
            if c==2:
                d=num
            elif c==0:
                m=num
        return [d,m]