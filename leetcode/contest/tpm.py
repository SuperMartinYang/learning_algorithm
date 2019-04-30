def cartesian(s):
    def helper(ss):
        i = 0
        n = len(ss)
        pre = ['']
        tmpCh = ''
        res = []
        while i < n:
            if ss[i].isalpha():
                while i < n and ss[i].isalpha():
                    tmpCh += ss[i]; i += 1
                # tmpCh * pre
                tmpPre = []
                for p in pre:
                    tmpPre.append(p + tmpCh)
                pre = tmpPre
                tmpCh = ''
            elif ss[i] == '{':
                subR = helper(ss[i+1:])
                tmpPre = []
                for p in pre:
                    for sr in subR[0]:
                        tmpPre.append(p + sr)
                pre = tmpPre
                i += subR[1] + 1
            elif ss[i] == ',':
                res += pre
                pre = ['']
                i += 1
            elif ss[i] == '}':
                if pre: res += pre
                return [res, i + 1]
        return [res , i + 1]
    return helper(s + ',')[0]

print(cartesian('{a,b}h{c,d},e'))