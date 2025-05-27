import timeit

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        results = False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 0:
                continue
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                results = True

        return results
    
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,34,3,4,5,7,23,12]
    
    def call():
        output = sol.threeConsecutiveOdds(arr)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    