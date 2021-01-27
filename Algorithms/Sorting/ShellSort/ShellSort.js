class ShellSort {

    static sort(arr) {
        const N = arr.length
        let H = 1
        while (H < Math.floor(N / 3)) {
            H = 3 * H + 1
        }
        while (H >= 1) {
            for (let i = H; i < N; i++) {
                for (let j = i; j >= H; j -= H) {
                    if (arr[j] < arr[j - H]) {
                        ShellSort.swap(arr, j, j - H)
                    } else {
                        break;
                    }
                }
            }
            H = Math.floor(H / 3)
        }
    }

    static swap(arr, x, y) {
        const temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    }

    static main() {
        const test1 = Array(20)
        const test2 = Array(20)
        for (let i = 0; i < 20; i++) {
            test1[i] = Math.floor(Math.random() * 100)
            test2[i] = Math.floor(Math.random() * 100)
        }
        console.log("Arrays before the sort:")
        console.log(test1)
        console.log(test2)
        ShellSort.sort(test1)
        ShellSort.sort(test2)
        console.log("Arrays after the sort:")
        console.log(test1)
        console.log(test2)
    }
}

ShellSort.main()