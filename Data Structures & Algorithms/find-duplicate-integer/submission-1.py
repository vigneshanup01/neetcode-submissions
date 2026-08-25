class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]


            if slow==fast:
                break

        pointer1=0
        pointer2=slow

        while pointer1!=pointer2:
            pointer1=nums[pointer1]
            pointer2=nums[pointer2]

        return pointer1 
        