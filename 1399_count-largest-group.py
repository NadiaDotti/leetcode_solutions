class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        data = {}
        while i <= n: 
            array = [int(c) for c in str(i)]
            sum_i = sum(array)
            if sum_i not in data:
                data[sum_i] = 1
            else:
                data[sum_i] += 1
            i = i + 1
        max_val = max(data.values())
        count = list(data.values()).count(max_val)
        return count


if __name__ == "__main__":
    sol = Solution()
    input_vals = [13, 2, 25, 30]
    for val in input_vals: 
        print("Value:", val)
        output = sol.countLargestGroup(val)
        print("Output:", output)
    