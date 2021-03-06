from collections import OrderedDict

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        dic = OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False