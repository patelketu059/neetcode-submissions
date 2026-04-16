class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        L, R = 0, len(nums1) - 1
        while True:
            M1 = L + (R - L) // 2
            M2 = half - M1 - 2

            A_L = nums1[M1] if M1 >= 0 else float('-inf')
            A_R = nums1[M1 + 1] if (M1 + 1) < len(nums1) else float('inf')
            B_L = nums2[M2] if M2 >= 0 else float('-inf')
            B_R = nums2[M2 + 1] if (M2 + 1) < len(nums2) else float('inf')

            if A_L <= B_R and B_L <= A_R:
                if total % 2 == 0: # EVEN
                    return (max(A_L, B_L) + min(A_R, B_R)) / 2
                else: # ODD
                    return min(A_R, B_R)
            if A_L > B_R:
                R = M1 - 1
            else:
                L = M1 + 1








        


