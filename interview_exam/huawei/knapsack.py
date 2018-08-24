import sys


def solver(vals, weights, cap):
    # put
    if not vals or not weights: return 0
    if cap <= 0: return 0
    if cap < weights[0]:
        res = solver(vals[1:], weights[1:], cap)
    else:
        res = max(vals[0] + solver(vals[1:], weights[1:], cap - weights[0]), solver(vals[1:], weights[1:], cap))
    return res


if __name__ == "__main__":
    # first line, value of each treasure
    vals = sys.stdin.readline().strip().split(',')
    weights = sys.stdin.readline().strip().split(',')
    cap = int(sys.stdin.readline().strip(),10)
    print(solver([int(i) for i in vals], [int(i) for i in weights], cap))
