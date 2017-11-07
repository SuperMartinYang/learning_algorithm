class Solution(object):
    def convert_to_title(self,n):
        '''

        :param n: int
        :return: str
        '''
        title = ''
        while n > 0:
            n -= 1
            a = n % 26
            n /= 26
            title = chr(a + 0x41) + title
        return title