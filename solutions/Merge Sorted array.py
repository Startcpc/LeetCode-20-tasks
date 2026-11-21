class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_p = m - 1
        nums2_p = n - 1

        for final in range(len(nums1) - 1,-1,-1):
            if  nums1_p >=0 and nums2_p >=0:
                if nums1[nums1_p] > nums2[nums2_p]:
                    nums1[final] = nums1[nums1_p]
                    nums1_p -= 1
                else:
                    nums1[final] = nums2[nums2_p]
                    nums2_p-=1
            elif nums1_p >= 0:
                nums1[final] = nums1[nums1_p]
                nums1_p -= 1
            else:
                nums1[final] = nums2[nums2_p]
                nums2_p -= 1
