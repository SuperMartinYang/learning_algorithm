#coding=utf-8
import sys

def minVal(points):
    if not points: return 0
    mid = (points[0] + points[-1]) // 2
    res = 0
    for p in points:
        res += abs(p - mid)
    return int(res)

def solver(points, k):
    if k == 1: return minVal(points)
    if len(points) == k: return 0
    res = float('inf')
    for i in range(1, len(points) - k + 2):
        res = min(res, minVal(points[:i]) + solver(points[i:], k - 1))
    return res

def tmp(a):
    a = a.split(' ')
    if not a:
        print(-1)
    points = [int(i) for i in a]
    return solver(points[:-1], points[-1])

print(tmp("1 2 3 4 400 1500 2"))