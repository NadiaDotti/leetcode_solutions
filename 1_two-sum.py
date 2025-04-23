class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            value = num
            # print(value)
            i = nums.index(value) + 1
            while i < len(nums):
                sum = value + nums[i]
                if target == sum:
                    return [nums.index(value), i]
                i = i + 1
        return


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 11, 7, 15]
    target = 9
    print("Value:", nums)
    output = sol.twoSum(nums, target)
    print("Output:", output)
    