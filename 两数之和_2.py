class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_list = []
        flag = True
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) & (nums[i] + nums[j] == target):
                    my_list.append(i)
                    my_list.append(j)
                    return my_list



nums = [3, 2, 4]
target = 6
solution = Solution()

print(solution.twoSum(nums, target))
