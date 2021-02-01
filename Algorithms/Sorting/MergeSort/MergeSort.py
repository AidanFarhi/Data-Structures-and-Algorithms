
class MergeSort:

    def sort(arr):
        aux = [None] * len(arr)
        MergeSort.__sort_helper(arr, aux, 0, len(arr) - 1)
    
    def __sort_helper(arr, aux, lo, hi):
        if hi <= lo:  # Base case
            return
        mid = lo + (hi - lo) // 2
        MergeSort.__sort_helper(arr, aux, lo, mid)        # Left half
        MergeSort.__sort_helper(arr, aux, mid + 1, hi)    # Right half
        MergeSort.__merge(arr, aux, lo, mid, hi)
    
    def __merge(arr, aux, lo, mid, hi):
        # Copy arr to aux array
        for n in range(lo, hi + 1):
            aux[n] = arr[n]
        # Now merge two sorted halves
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1


test1 = ["bibs", "zoo", "loss", "friend", "abby", "allan", "knife", "were", "waa", "loss"]
test2 = [6, 1, 7, 3, 4, 11, -66, 141, 664, -26, 1616, 2, 88, 1, 755, -2, -66, -2777]
MergeSort.sort(test1)
MergeSort.sort(test2)
print(test1)
print(test2)