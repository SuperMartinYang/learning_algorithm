class Solution(object):
    def valid_word_abbreviation(self, s, abbr):
        """
        s = "internationalization", abbr = "i12iz4n":
        :param st: str
        :param ab: str
        :return:
        """
        ps, pa = 0, 0
        while pa < len(abbr) and ps < len(s):
            if abbr[pa].isalpha():
                if abbr[pa] != s[ps]:
                    return False
            else:
                # get the val
                val = 0
                while pa < len(abbr) and abbr[pa].isdigit():
                    val = val * 10 + int(abbr[pa])
                    pa += 1
                ps += val
            ps += 1
            pa += 1
        return True

print(Solution().valid_word_abbreviation(s = "internationalization", abbr = "i12iz4n"))