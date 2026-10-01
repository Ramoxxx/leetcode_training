class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) <= 0:
            return

        backward_index = len(nums1)-1
        index = 0
        index2 = 0
        while index < m:
            num1 = nums1[index]
            nums1[backward_index] = num1
            backward_index -= 1 

            while index2 < len(nums2):
                num2 = nums2[index2]
                if num2 <= num1:
                    nums1[backward_index] = num1
                    backward_index -= 1
                index2 += 1

            index += 1            
            print(nums1)
        
        print(backward_index)

        nums1.reverse()
        

            
        