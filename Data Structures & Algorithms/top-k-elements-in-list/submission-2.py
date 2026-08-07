class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        heap=[]

        for num,freq in count.items():
            heapq.heappush(heap,(-freq,num))

        result=[]

        for _ in range(k):
            freq,num=heapq.heappop(heap)
            result.append(num)

        return result

        
        