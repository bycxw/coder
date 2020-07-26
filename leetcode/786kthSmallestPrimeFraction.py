# coding: utf-8
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        """binary search. O(N + logW)"""
        from fractions import Fraction

        def under(x):
            i = -1
            count = best = 0
            for j in range(1, len(A)):
                while A[i + 1] < A[j] * x:
                    i += 1
                count += i + 1
                if i >= 0:
                    best = max(best, Fraction(A[i], A[j]))
            return count, best
        low, high = 0.0, 1.0
        while high - low > 1e-7:
            mid = (high + low) / 2
            count_, ans = under(mid)
            if count_ == K:
                break
            elif count_ > K:
                high = mid
            else:
                low = mid
        return ans.numerator, ans.denominator