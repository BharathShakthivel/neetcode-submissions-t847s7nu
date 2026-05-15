class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res,max_heap = "",[]
        for count,char in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count!=0:
                heapq.heappush(max_heap,(count,char))
        while max_heap:
            count,char = heapq.heappop(max_heap)
            if len(res)>1 and res[-1]==res[-2]==char:
                if not max_heap:
                    break
                count_2,char_2 = heapq.heappop(max_heap)
                res+=char_2
                count_2+=1
                if count_2:
                    heapq.heappush(max_heap,(count_2,char_2))
            else:
                res+=char
                count+=1
            if count:
                heapq.heappush(max_heap,(count,char))
        return res

