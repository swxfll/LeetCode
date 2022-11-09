class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num = len(nums)
        for i in range(num):
            for j in range(i+1, num):
                if nums[i] + nums[j] == target:
                    return i, j



nums = [3, 2, 4]
target = 6
solution = Solution()

print(solution.twoSum(nums, target))
