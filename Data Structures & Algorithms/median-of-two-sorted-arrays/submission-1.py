class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        half = (m + n + 1) // 2

        l = 0
        r = m

        while l <= r:

            # Number of elements taken from nums1
            mid = (l + r) // 2

            # Number of elements taken from nums2
            x = half - mid

            # Boundaries of the two partitions
            left1 = float("-inf") if mid == 0 else nums1[mid - 1]
            right1 = float("inf") if mid == m else nums1[mid]

            left2 = float("-inf") if x == 0 else nums2[x - 1]
            right2 = float("inf") if x == n else nums2[x]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # We took too many elements from nums1
            elif left1 > right2:
                r = mid - 1

            # We took too few elements from nums1
            else:
                l = mid + 1