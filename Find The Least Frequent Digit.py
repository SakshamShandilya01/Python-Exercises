class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = {}
        while n > 0:
            digit = n % 10
            counts[digit] = counts.get(digit, 0) + 1
            n //= 10
        min_count = min(counts.values())
        counts = sorted(counts.items())
        for (digit, freq) in counts:
            if freq == min_count:
                return digit
