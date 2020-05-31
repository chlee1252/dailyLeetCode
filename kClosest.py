class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        def quick_select(lst, k):
            if k==0: return min(lst)
            if k==len(lst): return max(lst)
            if len(lst)<=10:
                return sorted(lst)[k-1]

            # select pivot (median of median)
            medians = [sorted(lst[i*5:i*5+5])[3] for i in range(len(lst)//5)]
            pivot = quick_select(medians, len(medians)//2)

            # separate lst by values smaller or larger than pivot
            smaller = [i for i in lst if i<=pivot]
            larger = [i for i in lst if i>pivot]

            # recursion
            if len(smaller)>=k:
                return quick_select(smaller, k)
            else:
                return quick_select(larger, k-len(smaller))
        distance = [i[0]**2+i[1]**2 for i in points]
        kth_order_stat = quick_select(distance, K)
        return [points[i] for i in range(len(points)) if distance[i] <= kth_order_stat]