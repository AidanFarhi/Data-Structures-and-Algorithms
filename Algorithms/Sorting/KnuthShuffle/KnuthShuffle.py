from random import randint


class KnuthShuffle:

    def shuffle(arr):
        N = len(arr)
        for i in range(N):
            r = randint(i, N - 1)
            arr[r], arr[i] = arr[i], arr[r]


def main():
    test1 = ["A", "B", "C", "D", "E", "F", "G"]
    test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    KnuthShuffle.shuffle(test1)
    KnuthShuffle.shuffle(test2)
    print(test1)
    print(test2)


main()