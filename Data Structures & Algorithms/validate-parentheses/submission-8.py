class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        i=0

        while i<len(s):
            
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])

            else:
                if len(stack)==0:
                    return False

                top=stack.pop()


                if s[i]==')' and top!='(':
                    return False

                if s[i]==']' and top!='[':
                    return False

                if s[i]=='}' and top!='{':
                    return False

            i+=1

        return not stack


        