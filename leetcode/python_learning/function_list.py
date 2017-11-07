import re
def build_match_and_apply(pattern, search, replace):
    '''
    The apply function is a function that takes one parameter,
    and calls re.sub() with the search and replace parameters that
    were passed to the build_match_and_apply_functions() function,
    and the word that was passed to the apply_rule() function you’re building.
    This technique of using the values of outside parameters within a dynamic function is called closures.
    :param pattern:
    :param search:
    :param replace:
    :return:
    '''
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


pattern = [(r'sxz$', '$', 'es'),
           (r'[^aeioudpgkrt]h$', '$', 'es'),
           (r'(qu|[^aeiou])y', 'y$', 'ies'),
           (r'$', '$', 's')]

# tuple of rule, if [0], do [1]. It contains not the name of function, but the object
rules = [build_match_and_apply(pattern, search, replace) for (pattern, search, replace) in pattern]

def plural(noun):
    '''
    use rules to do this job

    :param noun: need to deal
    :return: plural noun
    '''
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            apply_rule(noun)


