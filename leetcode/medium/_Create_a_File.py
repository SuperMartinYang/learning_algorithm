filename = input("Input File Name: ")
filename = '_'.join(filename.strip().split()) + '.py'
s = "class Solution(object):\n    def " + filename.lower()[:-3] + "(self):"
with open(filename, 'a') as f:
    f.writelines(s)
