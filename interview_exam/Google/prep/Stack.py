def Stack(heights):
    stack = []
    heights.append(0)
    res = 0
    for i in range(len(heights)):
        while not stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            s = stack[-1] if stack else -1
            res = max(res, h * (i - s - 1))
        stack.append(i)
    return res