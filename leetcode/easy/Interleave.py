def isInterleave(word1, word2, word3):
    '''
    word1= 'asdf'
    word2 = 'sadfa'
    word3 = 'assaddffa'
    :param word1: str
    :param word2: str
    :param word3: str
    :return: bool
    '''
    if word3 == '':
        if word1 == word2 == '':
            return True
        else:
            return False
    if word1[0] == word3[0]:
        return isInterleave(word1[1:], word2, word3[1:])
    elif word2[0] == word3[0]:
        return isInterleave(word1, word2[1:], word3[1:])
    else:
        return False



