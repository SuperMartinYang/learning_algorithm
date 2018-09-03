class Solution(object):
    def csv_formatter(self, csvLines):
        # get he max for each col
        res = ''
        colLen = [0] * len(max(csvLines, key=lambda x:len(x.split(','))).split(','))
        for line in csvLines:
            line = line.split(',')
            for i in range(len(line)):
                colLen[i] = max(colLen[i], len(line[i]))
        # print
        print(colLen)
        for line in csvLines:
            line = line.split(',')
            # print(line)
            printLine = ''
            for i in range(len(colLen)):
                wlen = len(line[i]) if i < len(line) else 0
                colW = ' ' * (colLen[i] - wlen) + (line[i] if i < len(line) else '') + ', '
                printLine += colW
            res += printLine[:-2] + '\n'
        return res

print(Solution().csv_formatter(['name,age,hobby', 'sskdgfkjprhenghuiyang,20,love bing', 'haobinghuang,,,,love yang']))