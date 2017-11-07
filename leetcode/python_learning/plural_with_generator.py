import re
def build_matches_and_apply_function(pattern, search, replace):
    def matches_rule(noun):
        return re.search(pattern, noun)
    def apply_rule(noun):
        return re.sub(search, replace, noun)
    return (matches_rule, apply_rule)

def rules(filename):
    with open(filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_matches_and_apply_function(pattern, search, replace)

def plural(filename,noun):
    rule_list = list(rules(filename))       #will not open file many time
    for matches_rule, apply_rule in rule_list:
        if matches_rule(noun):
            apply_rule(noun)
    raise ValueError('no match rule for {}'.format(noun))

