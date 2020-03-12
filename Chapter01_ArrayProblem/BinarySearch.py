def BinarySearch(arr, n, target):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            l = mid + 1
        elif arr[mid] < target:
            r = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    print(BinarySearch(arr, 5, target))
