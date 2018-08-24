import sys

dic = {}

def solver(target):
    # dfs get final type
    if target not in dic:
        return target
    return solver(dic[target].strip('*'))


if __name__ == "__main__":
    # first line, value of each treasure
    defines = sys.stdin.readline().strip().split(';')
    # parse defines to dict
    for d in defines:
        if not d: continue
        tmp = d.strip().split()
        if len(tmp) < 3: print("none")
        dic[tmp[-1]] = tmp[1]
    target = sys.stdin.readline().strip()
    if target not in dic: print('none')
    fin = solver(target)
    cntStar = dic[target].count('*')

    print(fin + ' *' * cntStar)
