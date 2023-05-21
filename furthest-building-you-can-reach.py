class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        size = len(heights)
        for i in range(size-1):
            gap = heights[i+1] - heights[i]
            if gap > 0:
                heappush(arr,gap)
            
            if len(arr) > ladders:
                val = heappop(arr)
                bricks -= val

            if bricks < 0:
                return i
            
        return size - 1