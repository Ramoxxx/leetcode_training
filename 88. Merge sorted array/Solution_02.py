class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        index1 = m - 1 # last nums1
        index2 = n - 1 # last nums2
        index3 = n + m - 1 # last of result list        

        while index2 >= 0:
            
            if index1 >= 0 and index2 >= 0 and nums1[index1] > nums2[index2]:
                nums1[index3] = nums1[index1]
                index1 -= 1
            else:
                nums1[index3] = nums2[index2]
                index2 -= 1
            
            index3 -= 1