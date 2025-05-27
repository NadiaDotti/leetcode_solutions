import timeit

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # SLOW SOLUTION
        # counter = 0
        # found_index = []
        # words_len = len(words)
        
        # found_single = False
        # for i in range(words_len):
        #     if i in found_index:
        #         continue
        #     found = False
        #     for j in range(i + 1, words_len):
        #         if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
        #             found_index += [j]
        #             counter += 4
        #             found = True
        #             break
        #     if not found_single and not found and words[i][0] == words[i][1]:
        #         counter += 2
        #         found_single = True
        #         continue 
                
        # return counter
        # FAST SOLUTION
        counter = 0
        word_count = {}
        single = False
        
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
                
        for word in word_count:
            rev = word[::-1]
            if rev in word_count and word != rev and word < rev:
                counter += min(word_count[word], word_count[word[::-1]]) * 4
                continue
            if word == rev:
                counter += word_count[word] // 2 * 4
                if word_count[word] % 2 == 1:
                    single = True
        
        if single:
            counter += 2
        
        return counter

    
if __name__ == "__main__":
    sol = Solution()
    words = ["ab","ty","yt","lc","cl","ab", "xx", "cc", "xx", "xx"]
    
    def call():
        output = sol.longestPalindrome(words)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")