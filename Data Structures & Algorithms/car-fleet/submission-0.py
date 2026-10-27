class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse=True)
        time = []
        result = []
        for p , s in cars:
            time = (target - p)/s
            if not result or time and result[-1] < time:
                    result.append(time)
        return len(result)
        