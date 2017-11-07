import re
def build_matches_and_apply_function(pattern, search, replace):
    def matches_rule(noun):
        return re.search(pattern, noun)
    def apply_rule(noun):
        return re.sub(search, replace, noun)
    return (matches_rule, apply_rule)

class LazyRules:
    '''
    why do we need to use cache?
    1st. if we call plural twice. At first, open a file, and find whether each line is appropriate
    2nd. But At the second time, Do we need to open this file again? And get the lines which we previously accessed?
    3rd. So what we need to do in order to save time and be efficient, we can cache lines we previously accessed, when we cached all lines, we do not need to access the file again
    4th. each time we use this instance, we only change the cache_index, cache and file will not changed( content, and file pointer used in readline )
    '''
    def __init__(self, filename):
        self.filename = open(filename, encoding='utf-8')
        self.cache = []
    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1           # go through cache
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.filename.closed:        # maybe this process will last a long time, so the file will not be closed, it may cause problems. Because file will only close when file pointer hits the end
            raise StopIteration         # or it will close when the program is exit
                                        # what we can do is to cache all the line at one time opening the file. Or we can read one line per time, and close the file, and save the file pointer by using
                                        # tell() and next time, open file, and use seek() to find the position
        line = self.filename.readline()
        if not line:
            self.filename.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        rule = build_matches_and_apply_function(pattern, search, replace)
        self.cache.append(rule)
        return rule

rules = LazyRules('plural_rules.txt')

def plural(noun):
    for matches_rule, apply_rule in rules():
        if matches_rule(noun):
            apply_rule(noun)
    raise ValueError('No match rule for {}'.format(noun))