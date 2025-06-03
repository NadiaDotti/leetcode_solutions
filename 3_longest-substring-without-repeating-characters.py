import timeit

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # good in memory, not the best in timing, maybe come back and try again
        max_arr = []
        array = []
        i = 0
        index = {}
        while i < len(s):
            if s[i] not in array:
                array += s[i]
                index[s[i]] = i
            else:
                if len(array) > len(max_arr):
                    max_arr = array
                array = [] 
                i = index[s[i]]
            i = i + 1
        array_len = len(array)
        max_len = len(max_arr)
        if array_len > max_len:
            return array_len
        return max_len

    
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    
    def call():
        output = sol.lengthOfLongestSubstring(s)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    