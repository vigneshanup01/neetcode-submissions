class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        res=[]
        max_heap=[]

        for num,freq in count.items():
            heapq.heappush(max_heap,(-freq,num))

        for _ in range(k):
            freq,num=heapq.heappop(max_heap)
            res.append(num)

        return res
        