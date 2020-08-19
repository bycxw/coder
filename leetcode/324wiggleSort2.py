# coding: utf-8
# https://leetcode.com/problems/wiggle-sort-ii/

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        O(n) time complexity. O(1) space complexity.
        kth smallest element
        quick sort. partition.
        """
        if not nums or len(nums) < 2:
            return
        def get_middle(l, r):
            i = l
            for j in range(l + 1, r + 1):
                if nums[j] < nums[l]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        def kth_smallest_element(k):
            l, r = 0, len(nums) - 1
            k -= 1
            while l < r:
                m = get_middle(l, r)
                if m < k:
                    l = m + 1
                elif m > k:
                    r = m - 1
                else:
                    break
            return nums[k]

        def A(i, n):
            return (2 * i + 1) % (n | 1)

        n = len(nums)
        m = (n + 1) >> 1
        median = kth_smallest_element(m)

        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[A(j, n)] > median:
                nums[A(j, n)], nums[A(i, n)] = nums[A(i, n)], nums[A(j, n)]
                j += 1
                i += 1
            elif nums[A(j, n)] < median:
                nums[A(j, n)], nums[A(k, n)] = nums[A(k, n)], nums[A(j, n)]
                k -= 1
            else:
                j += 1
