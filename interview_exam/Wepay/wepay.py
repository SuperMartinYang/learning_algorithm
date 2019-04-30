def alerter(inputs, windowSize, allowedIncrease):
    # preSum for average
    preSum = [0]
    for val in inputs:
        preSum.append(preSum[-1] + val)

    maxVal, maxIndex, maxCnt = float('-inf'), -1, 0
    i, j = 0, 0
    preAverage = 0

    while j <= len(inputs):
        if (j - i + 1 > windowSize):
            # condition 2
            average = (preSum[j] - preSum[i]) / windowSize
            if preAverage and average / preAverage >= allowedIncrease: return True
            preAverage = average
            if maxIndex == i:
                # update maxVal
                for idx in range(i + 1, j):
                    if inputs[idx] > maxVal:
                        maxVal = inputs[idx]
                        maxIndex = idx
                        maxCnt = 0
            # condition 1
            if maxVal / average >= allowedIncrease:
                maxCnt += 1
                if maxCnt == (windowSize if len(inputs) - maxIndex > windowSize else len(inputs) - maxIndex): return True
            i += 1
        elif inputs[j] > maxVal:
            maxVal = inputs[j]
            maxIndex = j
            maxCnt = 0
        print(maxVal, maxIndex)
        j += 1
                    
    return False

def alerter2(inputs, windowSize, allowedIncrease):
    if not inputs or not windowSize: return False
    i, j = 0, windowSize - 1
    preSum = [0]
    for val in inputs:
        preSum.append(preSum[-1] + val)

    preAverage = float("inf")
    maxVal, maxIdx, maxCnt = float('-inf'), -1, 0
    windowCnt = 0
    while j < len(inputs):
        if j - windowSize + 1 > maxIdx:
            maxVal, maxIdx = float('-inf'), -1
            for z in range(i, j + 1):
                if inputs[z] > maxVal:
                    maxVal = inputs[z]
                    maxIdx = z
                    maxCnt = 0
                    windowCnt = getWindow(len(inputs), z, windowSize)
        elif inputs[j] > maxVal:
            maxVal = inputs[j]
            maxIdx = j
            maxCnt = 0
            windowCnt = getWindow(len(inputs), j, windowSize)
        # condition 2
        average = (preSum[j + 1] - preSum[i]) / windowSize
        if not preAverage or average / preAverage > allowedIncrease: return True
        preAverage = min(preAverage, average)
        # condition 1
        if not average or maxVal / average > allowedIncrease:
            maxCnt += 1
            if maxCnt == windowCnt: return True

        j += 1
        i += 1
    return False

def getWindow(size, idx, window):
    if idx <= window - 1:
        return idx + 1
    elif idx >= size - window:
        return size - idx
    return window

print(alerter2([10,20,2,40,80,90,100], 4, 2))