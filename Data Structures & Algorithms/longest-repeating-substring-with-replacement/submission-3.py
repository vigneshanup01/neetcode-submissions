class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        maxFrequency=0
        count=Counter()

        left=0

        for right in range(len(s)):
            count[s[right]]+=1
            maxFrequency=max(maxFrequency,count[s[right]])

            while(right-left+1 - maxFrequency>k):
                count[s[left]]-=1
                left+=1

            longest=max(longest,right-left+1)

        return longest


        