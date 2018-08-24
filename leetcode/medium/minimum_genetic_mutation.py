class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        root = [start]
        bank = set(bank)
        level = 1
        while root:
            tmp_root = []
            for s in root:
                for i in range(len(s)):
                    for ch in "ATCG":
                        tmp_s = s[:i] + ch + s[i + 1:]
                        if tmp_s == end:
                            return level
                        if tmp_s in bank:
                            tmp_root.append(tmp_s)
                            bank.remove(tmp_s)
            root = tmp_root
            level += 1
        return -1


print(Solution().minMutation("AAAAACCC",
"AACCCCCC",
["AAAACCCC", "AAACCCCC", "AACCCCCC"]))