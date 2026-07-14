class Solution(object):
    def isAnagram(self, s, t):

        if (len(s) != len(t)):
            return False

        countS = {}
        countT = {}

        for ch in s:
            if ch in countS:
                countS[ch] += 1

            else:
                countS[ch] = 1

        for ch in t:
            if ch in countT:
                countT[ch] += 1

            else:
                countT[ch] = 1

        if countS == countT:
            return True

        else:
            return False








