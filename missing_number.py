class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Function call
sol = Solution()
result = sol.missingNumber(nums)

print("Missing Number:", result)