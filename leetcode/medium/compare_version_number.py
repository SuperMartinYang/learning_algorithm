class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0
        version1 = version1.split('.')
        version2 = version2.split('.')
        while i < len(version1) and i < len(version2):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            i += 1
        if i == len(version1) and i == len(version2):
            return 0
        elif i == len(version1):
            for k in (i, len(version2)):
                if int(version2[k]) != 0:
                    return -1
            return 0
        else:
            for k in (i, len(version1)):
                if int(version1[k]) != 0:
                    return 1
            return 0
        return 0

print(Solution().compareVersion("1.0.1", "1"))