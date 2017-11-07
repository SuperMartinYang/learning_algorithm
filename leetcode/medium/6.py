class Solution(object):
    def division(self,number):
        """
        :param number: need to get the divisions
        :return: divisions
        """
        i = 2
        list = []
        while i <= number:
            if self.prime(number):
                list.append(int(number))
                return list
            if number % i == 0:
                list.append(i)
                number /= i
                i = 2
            else:
                i += 1
        return list
    def prime(self,number):
        if number == 2:
            return True
        for i in range(2,int(pow(number,0.5))+1):
            if number % i == 0:
                return False
        return True

a = Solution()
print(a.prime(89))
print(a.division(178))