import collections
def taskSchedule(tasks, k):
    queue = collections.deque([' '] * k)
    res = []
    i = 0
    while i < len(tasks):
        if tasks[i] in queue:
            while tasks[i] in queue:
                res.append(queue.popleft())
                queue.append(' ')
            res.append(queue.pop())
            queue.append(tasks[i])
        else:
            res.append(queue.popleft())
            queue.append(tasks[i])
        i += 1
    return res[k:] + list(queue)


print(taskSchedule('ABCAADDCCD', 3))
