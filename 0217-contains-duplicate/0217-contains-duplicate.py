class Solution(object):
    def containsDuplicate(self, nums):
        list_len = len(nums)
        my_set = set(nums)
        set_len = len(my_set)
        if list_len == set_len :
            return False
        else :
            return True

        """
        :type nums: List[int]
        :rtype: bool
        """