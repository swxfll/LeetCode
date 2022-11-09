class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num = len(nums)
        my_list = []
        for i in range(num):
            for j in range(i + 1, num):
                if nums[i] + nums[j] == target:
                    my_list.append(i)
                    my_list.append(j)
                    return my_list


nums = [3, 2, 4]
target = 6
solution = Solution()

print(solution.twoSum(nums, target))
