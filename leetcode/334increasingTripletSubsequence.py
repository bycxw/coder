# coding: utf-8
# https://leetcode.com/problems/increasing-triplet-subsequence/


from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """O(n) time complexity."""
        first = second = float('inf')
        for num in nums:
            if num < first:
                first = num
            elif num < second:
                second = num
            else:
                return True
        return False


    def increasingTriplet2(self, nums: List[int]) -> bool:
        """EAFP: easier to ask for forgiveness than permission"""
        import bisect
        def increasingTripletCore(k):
            try:
                inc = [float('inf')] * (k - 1)
                for x in nums:
                    inc[bisect.bisect_left(inc, x)] = x
                return k == 0
            except:
                return True
        return increasingTripletCore(3)


    def increasingTriplet3(self, nums: List[int]) -> bool:
        """LBYL: look before you leap"""
        import bisect
        def increasingTripletCore(k):
            inc = [float('inf')] * (k - 1)
            for x in nums:
                i = bisect.bisect_left(inc, x)
                if i >= k - 1:
                    return True
                inc[i] = x
            return k == 0
        return increasingTripletCore(3)