class Solution(object):
    def findCircleNum(self, M):
        """
        Method:
            use DFS to visit all the node in the graph, and use mark to notify which node has been visited.
            since it is in the class, it's difficult to implement recursive method,(cuz there is two global variable)
            so, here, we use stack
        1st:
            init the mark and circleNum.
        2nd:
            judge whether each node in the mark, whether it is 0, if it is, start from that node, and go through the edge connected to that node(DFS)
            since it may connected to other node meantime, so we put start_node to the stack, deal other edge, when we go back from the sub_node
        3rd:
            go through sub_node, if it has not been visited, than push it into stack and set the mark
            if this node has no subroot anymore, pop out this node
        recursively do 2nd step


        :type M: List[List[int]]
        :rtype: int
        """
        # DFS       mark 0 -> use loop to do -> change mark 1 ->
        N = len(M)
        mark = [0] * N
        circleNum = 0
        for i in range(N):  # multi-circle, cannot be done from one root
            if mark[i] == 0:
                stack = []
                start = i
                stack.append(start)
                mark[start] = 1
                while stack:
                    # do DFS
                    tmp = stack[-1]
                    i = 0
                    while i < N:
                        if M[tmp][i] == 1 and mark[i] == 0:
                            mark[i] = 1
                            stack.append(i)
                            break
                        i += 1
                    if i == N:
                        stack.pop()
                circleNum += 1

        return circleNum



M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
s = Solution()
print(s.findCircleNum(M))