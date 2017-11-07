class Solution(object):
    def majorityElement(self, nums):
        """
        get the majority element, since majority element is more than [n/2], so when the element is majority elemnt, it will be positive, if not, it will be negative. so ,after all , the last
        positive number is majority element
        :type nums: List[int]
        :rtype: int
        """
        # assume that the first element is the majority
        maj_ele = nums[0]
        ele_count = 1
        num_len = len(nums)
        for i in range(1, num_len):
            if ele_count == 0:
                maj_ele = nums[i]
                ele_count = 1
            elif maj_ele == nums[i]:
                ele_count += 1
            else:
                ele_count -= 1

        return maj_ele
