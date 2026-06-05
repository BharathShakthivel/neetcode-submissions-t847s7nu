class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time - n logn
        if (len(hand) % groupSize) != 0:
            return False
        freq = {}
        min_heap = []
        for i in hand:
            freq[i] = 1 + freq.get(i,0)
        for k in freq.keys():
            heapq.heappush(min_heap,k)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i]-=1
                if freq[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

                
