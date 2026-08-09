class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1=Counter(s1)
        countWindow={}

        left=0

        for right in range(len(s2)):
            countWindow[s2[right]]=countWindow.get(s2[right],0)+1

            if right-left+1>len(s1):

                countWindow[s2[left]]-=1

                if countWindow[s2[left]]==0:
                    del countWindow[s2[left]]
                left+=1

            if countWindow==counts1:
                return True
        return False


        
        