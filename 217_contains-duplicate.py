import timeit

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # not the best in memory, maybe come back and try a different approach
        a = list(set(nums))
        if len(a) < len(nums):
            return True
        return False
    
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    
    def call():
        output = sol.containsDuplicate(nums)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    