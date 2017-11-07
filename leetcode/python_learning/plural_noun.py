import re

def plural(noun):
    if re.search(r'[^sxz]$', noun):
        return re.sub(r'$', 'es', noun)
    elif re.search(r'[^aeioudgkprt]h$', noun):
        return re.sub(r'$', 'es', noun)
    elif re.search(r'[^aeiou]y$', noun):
        return re.sub(r'y$', 'ies', noun)
    else:
        return noun+'s'