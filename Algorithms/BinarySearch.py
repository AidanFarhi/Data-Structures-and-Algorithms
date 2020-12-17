class BinarySearch:
    # Returns first index that target is found at or -1 if not in array
    def binary_search(self, arr, target):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > target:
                hi = mid - 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                return mid
        return - 1

# Tests
BS = BinarySearch()
test_array = [0] * 10000000
for i in range(10000000):
    test_array[i] = i
print(BS.binary_search(test_array, 15555))
print(BS.binary_search(test_array, -1515))
print(BS.binary_search(test_array, 155))
print(BS.binary_search(test_array, 5959959))
print(BS.binary_search(test_array, 0))
print(BS.binary_search(test_array, -1))
