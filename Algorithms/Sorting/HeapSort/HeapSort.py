class HeapSort:

    def sort(arr):
        N = len(arr) - 1
        HeapSort.heapify(arr, N)
        while N > 0:
            arr[0], arr[N] = arr[N], arr[0]
            N -= 1
            HeapSort.sink(arr, 0, N)

    def heapify(arr, N):
        # N//2 here because everything in the right half of array is a subtree of size 1
        for i in range(N//2, -1, -1):
            HeapSort.sink(arr, i, N)
    
    def sink(arr, i, N):
        while 2*i <= N:
            j = 2*i  # left child
            if j < N and arr[j] < arr[j + 1]:  # find out which child is larger
                j += 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
            else:
                break


def main():
    test1 = [5, 1, -66, 141, 667, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22]
    test2 = ["J", "Y", "B", "N", "Q", "P", "A", "R", "H", "G", "Y", "W", "U", "Z", "K"]
    HeapSort.sort(test1)
    HeapSort.sort(test2)
    print(test1)
    print(test2)


main()