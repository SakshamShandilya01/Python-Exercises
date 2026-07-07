class Solution(object):
    def maximum69Number(self, num):

        number = list(str(num))

        for i in range(len(number)):
            if number[i] == '6':
                number[i] = '9'
                break

        result = ""

        for j in number:
            result += j

        return int(result)