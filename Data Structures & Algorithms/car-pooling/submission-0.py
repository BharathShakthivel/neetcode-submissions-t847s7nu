class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_heap =[] 
        for trip in trips:
            heapq.heappush(trip_heap,[trip[1],1,trip[0]])
            heapq.heappush(trip_heap,[trip[2],0,trip[0]])
        while trip_heap:
            trip_point,cur_type,cur_capacity = heapq.heappop(trip_heap)
            if cur_type == 0:
                capacity+= cur_capacity
            else:
                capacity-= cur_capacity
            if capacity<0:
                return False
        return True