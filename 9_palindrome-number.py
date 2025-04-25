import timeit

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num = str(x)
        str_num_len = len(str_num)
        str_num_count = str_num_len - 1
        
        for i in range(str_num_len // 2):
            if str_num[i] != str_num[str_num_count]:
                return False
            str_num_count -= 1
            
        return True
    
    
if __name__ == "__main__":
    sol = Solution()
    nums = 121
    
    def call():
        output = sol.isPalindrome(nums)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    