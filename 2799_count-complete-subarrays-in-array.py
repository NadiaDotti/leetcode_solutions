from collections import defaultdict

class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        distinct_item = set(nums)
        distinct_item_len = len(distinct_item)
        nums_len = len(nums)
        counter = 0
        
        for start in range(nums_len):
            freq = defaultdict(int)
            uniq = 0
            
            for end in range(start, nums_len):
                if freq[nums[end]] == 0:
                    uniq += 1
                freq[nums[end]] += 1

                if uniq == distinct_item_len:
                    counter += 1
        return counter
    
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,1,2,2]
    output = sol.countCompleteSubarrays(nums)
    print("Output:", output)
    