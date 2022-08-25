import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.addToHeap(num)
        
    def addToHeap(self, num : int):
        heapq.heappush(self.heap , num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        self.addToHeap(val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
        

# https://leetcode.com/problems/kth-largest-element-in-a-stream/
if __name__ == "__main__":
    pass
