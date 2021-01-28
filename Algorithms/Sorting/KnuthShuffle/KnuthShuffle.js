
class KnuthShuffle {

    static shuffle(arr) {
        const N = arr.length
        for (let i = 0; i < N; i++) {
            const r = Math.floor(Math.random() * (N - i) + i);
            KnuthShuffle.swap(arr, r, i)
        }
    }

    static swap(arr, i, j) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}


function main() {
    const test1 = ["A", "B", "C", "D", "E", "F", "G"]
    const test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    KnuthShuffle.shuffle(test1)
    KnuthShuffle.shuffle(test2)
    console.log(test1)
    console.log(test2)
}


main()