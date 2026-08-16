class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window=Counter()

        satisfied=0
        required=len(need)
        left=0

        bestLength=float("inf")
        bestStart=0

        for right in range(len(s)):
            window[s[right]]+=1

            if s[right] in need and window[s[right]]==need[s[right]]:
                satisfied+=1

                while satisfied==required:
                    windowLength=right-left+1

                    if windowLength<bestLength:
                        bestLength=windowLength
                        bestStart=left

                    window[s[left]]-=1

                    if s[left] in need and window[s[left]]<need[s[left]]:
                        satisfied-=1
                    
                    left+=1

        if bestLength==float("inf"):
            return ""

        return s[bestStart:bestStart+bestLength]

        
                        

        