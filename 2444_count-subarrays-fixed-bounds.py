import timeit

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        nums_len = len(nums)
        counter = 0
        
        min_index = -1
        max_index = -1
        last_invalid = -1
        for n in range(nums_len):
            num = nums[n]
            if not (minK <= num <= maxK):
                last_invalid = n
            
            if num == maxK:
                max_index = n
            if num == minK:
                min_index = n
            
            valid_start = min(min_index, max_index)
            if valid_start > last_invalid:
                counter += valid_start - last_invalid
        return counter
    
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    
    def call():
        output = sol.countSubarrays(nums, minK, maxK)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    