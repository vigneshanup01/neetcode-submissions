class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need=Counter(t)
        window=Counter()

        satisfied=0
        required=len(need)

        left=0

        bestStart=0
        bestLength=float("inf")

        for right in range(len(s)):
            window[s[right]]+=1

            if s[right] in need and window[s[right]]==need[s[right]]:
                satisfied+=1

            while satisfied==required:
                windowLength=right-left+1

                if windowLength<bestLength:
                    bestLength=windowLength
                    bestStart=left

                leftChar=s[left]
                window[leftChar]-=1

                if leftChar in need and window[leftChar]<need[leftChar]:
                    satisfied-=1

                left+=1

        if bestLength==float("inf"):
                return ""
            
        return s[bestStart:bestStart+bestLength]

            

            

        



        