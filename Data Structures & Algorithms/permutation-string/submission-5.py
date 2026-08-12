class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1=Counter()
        countWindow=Counter()

        for char in s1:
            counts1[char]+=1
        left=0

        for right in range(len(s2)):

            countWindow[s2[right]]+=1

            if right-left+1>len(s1):
                countWindow[s2[left]]-=1

                if countWindow[s2[left]]==0:
                    del countWindow[s2[left]]

                left+=1

            if countWindow==counts1:
                    return True

        return False



        