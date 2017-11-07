import re
def build_matches_and_apply_function(pattern, search, replace):
    def matches_rule(noun):
        return re.search(pattern, noun)
    def apply_rule(noun):
        return re.sub(search, replace, noun)
rules = []
# with can define a file context, after this context, file will automaticaly closed
with open('plural-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_matches_and_apply_function(pattern, search, replace))



def plural(noun):
    '''
    use rules to do this job

    :param noun: need to deal
    :return: plural noun
    '''
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            apply_rule(noun)
