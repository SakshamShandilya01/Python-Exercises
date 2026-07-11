class Solution(object):
    def minDays(self, bloomDay, m, k):

        n = len(bloomDay)

        if(m * k > n):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while(low <= high):

            mid = (low + high) // 2

            count = 0
            bouquet = 0

            for i in range(len(bloomDay)):

                if(bloomDay[i] <= mid):
                    count += 1
                else:
                    count = 0

                if(count == k):
                    bouquet += 1
                    count = 0

            if(bouquet >= m):
                high = mid - 1
            else:
                low = mid + 1

        return low