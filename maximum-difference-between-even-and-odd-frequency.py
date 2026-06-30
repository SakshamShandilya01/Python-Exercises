class Solution(object):
    def maxDifference(self, s):

        max_odd = 0
        max_even = len(s) + 1

        for i in range(len(s)):

            count = 0

            for j in range(len(s)):
                if s[i] == s[j]:
                    count = count + 1

            already_counted = False

            for k in range(i):
                if s[i] == s[k]:
                    already_counted = True

            if already_counted == False:

                if count % 2 == 0:
                    if count < max_even:
                        max_even = count

                else:
                    if count > max_odd:
                        max_odd = count

        return max_odd - max_even