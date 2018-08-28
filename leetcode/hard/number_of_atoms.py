import collections
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # helper
        def helper(ss):
            """
            : rtype: list[] => 0: dic of freq, length: start to ')'
            """
            fre = collections.defaultdict(int)
            i = 0
            while i < len(ss):
                if ss[i].isalpha() and 'A' <= ss[i] <= 'Z':
                    # get item
                    cnt = i + 1
                    while cnt < len(ss) and ss[cnt].isalpha() and 'a' <= ss[cnt] <= 'z':
                        cnt += 1
                    item = ss[i:cnt]
                    # get num
                    i = cnt
                    while cnt < len(ss) and ss[cnt].isdigit():
                        cnt += 1
                    f = int(ss[i:cnt]) if i != cnt else 1
                    fre[item] += f
                    i = cnt
                elif ss[i] == '(':
                    i += 1
                    pres = helper(ss[i:])
                    # update i
                    i += pres[1] + 1
                    # get cnt
                    cnt = i
                    while cnt < len(ss) and ss[cnt].isdigit():
                        cnt += 1
                    f = int(ss[i:cnt]) if i != cnt else 1
                    i = cnt
                    # update fre
                    for key, val in pres[0].items():
                        fre[key] += val * f
                elif ss[i] == ')':
                    return [fre, i]
            return [fre, i]
        freq = helper(formula)[0]
        res = ''
        for key, val in freq.items():
            res += key + (str(val) if val > 1 else '')
        return res

Solution().countOfAtoms("H11He49NO35B7N46Li20")

Solution().countOfAtoms("H2(OH(SO3)2)2")

