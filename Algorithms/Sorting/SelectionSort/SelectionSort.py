
class SelectionSort:

    def sort(arr):
        N = len(arr)
        for i in range(N):
            min = i
            for j in range(i + 1, N):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]


test1 = ["B", "C", "X", "A", "P"]
test2 = [5, -11, 555, -61, 636, -99]

SelectionSort.sort(test1)
SelectionSort.sort(test2)

print(test1)
print(test2)