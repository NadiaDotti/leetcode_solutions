import timeit

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        counter = 0
        for i in range(nums_len):
            final_pos = i + 2
            if final_pos >= nums_len:
                break
            if float(nums[i]) + float(nums[final_pos]) == (float(nums[final_pos - 1]) / 2):
                counter += 1
        return counter
    
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1,4,1]
    
    def call():
        output = sol.countSubarrays(nums)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    