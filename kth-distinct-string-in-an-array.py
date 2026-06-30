class Solution:
    def kthDistinct(self, arr, k):
        count = {}

        for word in arr:
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

        distinct = []

        for word in arr:
            if count[word] == 1:
                distinct.append(word)

        if k <= len(distinct):
            return distinct[k - 1]

        return ""