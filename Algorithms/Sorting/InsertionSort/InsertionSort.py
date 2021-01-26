
class InsertionSort:

    def sort(arr):
        N = len(arr)
        for i in range(N):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break


test1 = ["B", "C", "X", "A", "P"]
test2 = [5, -11, 555, -61, 636, -99]

InsertionSort.sort(test1)
InsertionSort.sort(test2)

print(test1)
print(test2)
