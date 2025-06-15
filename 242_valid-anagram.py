import timeit

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map = {}
        for letter in s:
            map[letter] = map.get(letter, 0) + 1
            
        for letter in t:
            if map.get(letter) and map[letter] > 0:
                map[letter] -= 1
            else:
                return False
        
        return True
        
    
if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    
    def call():
        output = sol.isAnagram(s, t)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    