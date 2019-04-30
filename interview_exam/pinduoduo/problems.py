import heapq
class Solutions:
    def problem1(self, grid):
        """
        include most 1, start from top-right, when meet 1, go left, when meet 0, go down
        Time complexity: O(m + n)       # m: rows, n: cols
        Space complexity: O(1)          # not create space
        param: grid: list[list[int]]
        rtype: list[int]
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        if n == 0: return []
        i, j = 0, n   # top-right
        maxCnt, res = 0, []
        while i < m:
            if 0 <= j < n and grid[i][j] == 0:                              # meet 0, go down
                i += 1; continue
            while j - 1 >= 0 and grid[i][j - 1] == 1: j -= 1                # meet 1, keep go right
            if n - j != 0 and n - j == maxCnt: res.append(i + 1)            # update maxCnt
            elif n - j > maxCnt: res, maxCnt = [i + 1], n - j
            i += 1
        return res

    def problem2(self, expr):
        """
        valid brackets, use stack and record the prev priority
        Time Compexity: O(n)        # iterate expr, n: chars in expr
        Space Complexity: O(n)      # stack space
        param: expr: str
        rtype: bool
        """
        priority = {'(': 0, '[': 1, '{': 2}
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        left, right = '([{', '}])'
        for ch in expr:
            if ch in left:
                if not stack or (priority[ch] < priority[stack[-1]] or priority[ch] == priority[stack[-1]] == 2):
                    stack.append(ch)
                else: return False      # priority error
            elif ch in right:
                if not stack or match[ch] != stack[-1]:
                    return False        # match error
                else: stack.pop()
        return not stack                # empty or not
    
    def problem3(self, robot):
        """
        get area of room, sweep by robot, dfs to visited all area, return visited set's length
        Time Complexity: O(n)           # N area, visit all nodes, each node has 4 edge, exactly complexity could be 4N
        Space Compexity: O(n)           # function stack space, also visited set
        param: robot: object
        rtype: int
        """
        visited = set()      # visited set
        direction = {
            (0, 1): 0,      # left
            (1, 0): 1,      # down
            (0, -1): 2,     # right
            (-1, 0): 3      # up
        }
        def sweep(i, j):
            visited.add(i, j)
            for p, q in direction.keys():
                if (i + p, j + q) not in visited and robot.move(direction[p, q]):       # can move to? visited?
                    sweep(i + p, j + q)
                    robot.move(direction[-p, -q])   # move back
        sweep(0, 0)
        return len(visited)         # visited cnt would be the area

    def problem4(self, arrs):
        """
        smallest range includes at least one element in each arr, use priority queue, get min at once, update the range
        Time complexity: O(mnlogm)          # m: row cnt, n: col cnt, logn for heapq
        Space complexity: O(m)              # for heap
        param: arrs: list[list[int]]
        rtype: list
        """
        hp = [[arrs[i][0], i, 0] for i in range(len(arrs))]
        heapq.heapify(hp)
        res = float('-inf'), float('inf')        # init range
        right = max(row[0] for row in arrs)
        # shink range
        while hp:
            left, i, j = heapq.heappop(hp)
            if right - left < res[1] - res[0]:
                res = left, right
            if j + 1 == len(arrs[i]):
                return res
            v = arrs[i][j + 1]
            right = max(right, v)
            heapq.heappush(hp, [v, i, j + 1])
        

if __name__ == '__main__':
    s = Solutions()
    print(s.problem1([[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]])); print(s.problem1([[0]]))
    print(s.problem2('{[(2 + 3) * (1-3)]+4}*(14-3)'))
    print(s.problem4([[1,3,5], [4,8], [2,5]]))