def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        # 값이 중간 값보다 작은 경우 -> 왼쪽
        elif array[mid] > target:
            end = mid - 1
        # 값이 중간 값보다 큰 경우 -> 오른쪽
        else:
            start = mid + 1
        
    return -1
