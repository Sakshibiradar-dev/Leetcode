class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i       
        