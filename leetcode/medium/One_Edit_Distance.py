class Solution(object):
    def one_edit_distance(self, str1, str2):
        dif = abs(len(str1) - len(str2))
        if dif > 1: return False
        if dif == 1:
            # long1, short2
            str1, str2 = max(str1, str2, key=len), min(str1, str2, key=len)
            p1, p2 = 0, 0
            cnt = 0
            while p1 < len(str1) and p2 < len(str2):
                if str1[p1] == str2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    if cnt > 0:
                        return False
                    cnt += 1
                    p1 += 1
            return True
        else:
            cnt = 0
            i = 0
            while i < len(str1):
                if str1[i] != str2[i]:
                    cnt += 1
                    if cnt > 1: return False
            return True


