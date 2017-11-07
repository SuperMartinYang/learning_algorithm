def decipher(cipher_text):
    plain_text = ''
    for i in range(0,26):
        for j in cipher_text:
            plain_text += chr((ord(j) - 65 - i) % 26 + 65)
        print('key:{0}\t plain_text:{1}'.format(i,plain_text))
        plain_text = ''

def count_num(cipher_text):
    for i in cipher_text:
        print('{} has {}'.format(i,cipher_text.count(i)))
decipher('TEBKFKQEBZLROPBLCERJXKBSBKQP')
#
# def count_fre(cipher_text):
#     for i in cipher_text:
#         print('{} has {}'.format(i,cipher_text.count(i) / 28))
# count_fre('TEBKFKQEBZLROPBLCERJXKBSBKQP')
#
# print(set('TEBKFKQEBZLROPBLCERJXKBSBKQP'))
# print(len('TEBKFKQEBZLROPBLCERJXKBSBKQP'))
#
# dict = {'a':8.167,
# 'b':1.492,
# 'c':2.782,
# 'd':4.253,
# 'e':12.702,
# 'f':2.228,
# 'g':2.015,
# 'h':6.094,
# 'i':6.966,
# 'j':0.153,
# 'k':0.772,
# 'l':4.025,
# 'm':2.406,
# 'n':6.749,
# 'o':7.507,
# 'p':1.929,
# 'q':0.095,
# 'r':5.987,
# 's':6.327,
# 't':9.056,
# 'u':2.758,
# 'v':0.978,
# 'w':2.360,
# 'x':0.150,
# 'y':1.974,
# 'z':0.074}
#
# dict2 = {
# 'T':0.036,
# 'E':0.107,
# 'B':0.179,
# 'F':0.036,
# 'K':0.143,
# 'Q':0.071,
# 'Z':0.036,
# 'R':0.071,
# 'O':0.036,
# 'J':0.036,
# 'L':0.071,
# 'P':0.071,
# 'C':0.036,
# 'S':0.036,
# 'X':0.036
# }
# sum = 0
# for i in range(0,26):
#     for key in dict2.keys():
#         indx = ord(key)
#         p = dict[chr((indx - 65 - i) % 26 + 97)] / 100
#         sum += dict2[key] * p
#     print('ꝕ({0})={1:.3f}\t'.format(i,sum))
#     sum = 0

