class Solution(object):
    def findLucky(self, arr):

        answer = -1

        for i in arr:
            count = 0

            for j in arr:
                if i == j:
                    count += 1

            if count == i:
                if i > answer:
                    answer = i

        return answer
