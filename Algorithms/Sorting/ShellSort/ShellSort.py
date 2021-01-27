class ShellSort:

    def sort(arr):
        N = len(arr)
        H = 1
        while H < N // 3:
            H = 3 * H + 1
        while H >= 1:
            for i in range(H, N):
                for j in range(i, H - 1, -H):
                    if (arr[j] < arr[j - H]):
                        arr[j], arr[j - H] = arr[j - H], arr[j]
                    else:
                        break
            H = H // 3
    
    def main():
        test1 = ["B", "C", "X", "A", "P"]
        test2 = [5, -11, 555, -61, 636, -99]
        ShellSort.sort(test1)
        ShellSort.sort(test2)
        print(test1)
        print(test2)


ShellSort.main()