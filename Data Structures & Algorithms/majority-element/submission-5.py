class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq ={}
        # res, count =0,0
        # for n in nums:
        #     freq[n] = 1 + freq.get(n,0)
        #     if freq[n] > count:
        #         res = n
        #     count = max(count,freq[n])
        # return res

        # Boyer-moore voting algorithm
        count = 0
        res = 0
        for n in nums:
            if count == 0:
                res = n
            count+= (1 if n == res else -1)  # ternary operator
        return res
            
            
