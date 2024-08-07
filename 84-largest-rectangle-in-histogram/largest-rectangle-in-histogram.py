class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        smaller lines become a "limiting" item
        1 2 3 4 5 ... -> 9 => 1 1 1 1 1
        brute-force O(n^3)
        optimize O(n^2)

        need: max area

        stack (monotonous?) -> invariant 
        heights[i]
        if a new given line is shorter than the top of the stack, then extend this given line to the line at the top of the stack, min(heights[i], stack[-1].height), starting_idx = stack[-1].starting_idx
        otherwise, 
        e.g. 2 4 ... max area up to stack[-1] + min(stack[-1].height, heights[i])

        seen = [] # (line index, height)
        max_area = 0

        """

        stack = [] # height, idx
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        return max_area