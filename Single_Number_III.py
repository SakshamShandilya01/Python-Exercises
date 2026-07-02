class Solution(object):
    def singleNumber(self, nums):
        l=[]
        for num in nums:
            if num in l:
                l.remove(num)
            else:
                l.append(num)
        return l