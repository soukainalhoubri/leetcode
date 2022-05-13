class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[i+m]=nums2[i]
        return nums1.sort()