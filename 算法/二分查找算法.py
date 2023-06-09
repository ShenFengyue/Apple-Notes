
# 这个比较简单，就不写注释了。

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # 目标元素不存在

# 示例用法
arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
if result != -1:
    print("目标元素在索引", result, "处")
else:
    print("目标元素不存在")

