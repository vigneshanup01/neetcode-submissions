class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return ''.join(res)


    def decode(self, s: str) -> List[str]:

        res=[]
        i=0
        while i<len(s):

            j=i

            while(s[j]!='#'):
                j+=1

            length=int(s[i:j])

            j+=1

            word=s[j:j+length]

            res.append(word)

            i=j+length
        return res