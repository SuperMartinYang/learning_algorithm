class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            ori = i
            j = ori
            cnt = 0
            visited = [False for _ in range(len(nums))]
            flag = True if nums[ori] > 0 else False
            while not visited[j]:
                visited[j] = True
                j = (j + nums[j]) % len(nums)
                cnt += 1
                if j == ori and cnt > 1:
                    return True
                tmp_flag = True if nums[j] > 0 else False
                if tmp_flag != flag:
                    break
        return False