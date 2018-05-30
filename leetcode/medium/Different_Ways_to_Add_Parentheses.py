import re
class Solution(object):
    def diffWaysToCompute(self, input_):
        """
        :type input: str
        :rtype: List[int]
        """
        if len(re.split('\D', input_)) <= 2:
            return [eval(input_)]
        res = []
        i = 1
        while i < len(input_) + 1:
            while i < len(input_) and input_[i].isdigit():
                i += 1
            pre = input_[:i]
            post = input_[i + 1:]
            if not post:
                return res
            for item_i in self.diffWaysToCompute(pre):
                for item_j in self.diffWaysToCompute(post):
                    res.append(eval(str(item_i) + input_[i] + str(item_j)))
            i += 2
        return res


print(Solution().diffWaysToCompute('2-11-1*3'))