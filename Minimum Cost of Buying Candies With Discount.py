class Solution(object):
    def minimumCost(self, cost):

        cost.sort(reverse=True)

        total = 0

        for i in range(0, len(cost), 3):

            total += cost[i]

            if i + 1 < len(cost):
                total += cost[i + 1]

        return total