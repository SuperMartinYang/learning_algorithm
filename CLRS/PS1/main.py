import sys
import peak
import trace
import algorithms
import json
import utils

#########################################################################
########################## The main method ##############################
#########################################################################

def loadProblem(file = 'problem.py', variable = 'problemMatrix'):
    """
    loads a matrix from a python file, and constructs a PeakProblem from it
    :param file:
    :param variable:
    :return:
    """

    namespace = dict()
    with open(file) as handle:
        exec(handle.read(), namespace)
    return peak.createProblem(namespace[variable])

def main():
    if len(sys.argv) > 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename('problem.py'))

    # run all algorithms, gathering the traces and printing out the results as we go
    algorithmList = [('Algorithm1', algorithms.algorithm1),
                     ('Algorithm2', algorithms.algorithm2),
                     ('Algorithm3', algorithms.algorithm3),
                     ('Algorithm4', algorithms.algorithm4)]

    steps = []

    for (name, function) in algorithmList:
        tracer = trace.TraceRecord()
        peak = function(problem, trace = tracer)
        steps.append(tracer.sequence)

        status = "is Not a peak (INCORRECT!)"

        if problem.isPeak(peak):
            status = "is a peak"

        print(name + " : " + str(peak) + " => " + status)

        # write the trace out to a file
        with open("trace.jsonp", "w") as traceFile:
            traceFile.write("parse(")

            json.dump({
                "input" : problem.array,
                "steps" : steps
            }, traceFile)

if __name__ == '__main__':
    main()