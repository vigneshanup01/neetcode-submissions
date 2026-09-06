class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]

        max_area=0

        for i in range(len(heights)):

            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]

                if stack:
                    width=i-stack[-1]-1


                else:

                    width=i

                area=height*width

                max_area=max(max_area,area)

            stack.append(i)  

        while stack:
            height=heights[stack.pop()]

            if stack:
                width=len(heights)-stack[-1]-1

            else:
                width=len(heights)

            area=height*width

            max_area=max(max_area,area)

        return max_area

        
        