level = ((90,'a'),
         (80,'b'),
         (70,'c'),
         (60,'d'),)
def grade(no):
    for score, degree in level:
        if no > score:
            return degree
    return 'e'

print(grade(71))