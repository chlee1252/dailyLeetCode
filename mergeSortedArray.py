class Solution:
  def merge(self, nums1: [int], nums2: [int], m: int, n: int) -> None:
    # Not a good solution, but it passes. Pythonic Way
    nums1[m:] = nums2[:n]
    nums1.sort()

    # Better Solution
    while n > 0:
      if m <= 0 or nums2[n-1] >= nums1[m-1]:
        nums1[m+n-1] = nums2[n-1]
        n -= 1
      else:
        nums1[m+n-1] = nums1[m-1]
        m -= 1