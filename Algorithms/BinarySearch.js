class BinarySearch {
    // Returns first index found of target or -1 if not in array
    binarySearch(arr, target) {
        let lo = 0
        let hi = arr.length - 1
        while (lo <= hi) {
            let mid = Math.floor(lo + (hi - lo) / 2)
            if (arr[mid] > target) {
                hi = mid - 1
            } else if (arr[mid] < target) {
                lo = mid + 1
            } else {
                return mid
            } 
        }
        return -1
    }
}

// Tests
const BS = new BinarySearch()
const testArray = Array(10000000)
for (let i = 0; i < 10000000; i++) {
    testArray[i] = i;
}
console.log(BS.binarySearch(testArray, 5353))
console.log(BS.binarySearch(testArray, -5353))
console.log(BS.binarySearch(testArray, 67373))
console.log(BS.binarySearch(testArray, 53))
console.log(BS.binarySearch(testArray, -8))
console.log(BS.binarySearch(testArray, 0))
