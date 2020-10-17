  
function sudokuValidator(solution) {
    let check = [1,2,3,4,5,6,7,8,9]
    let dupeCheck = []
    let subGroups = subGroupGenerator(solution)
  
    // generates subgroups
    function subGroupGenerator(solution) {
        const ranges = [
            [3, 3],[3, 6],[3, 9],
            [6, 3],[6, 6],[6, 9],
            [9, 3],[9, 6],[9, 9]
        ]
        const subGroups = []
        for (let i = 0; i < ranges.length; i++) {
            const subGroup = []
            let range = ranges[i]
            for (let j = range[0] - 3; j < range[0]; j++) {
                for (let k = range[1] - 3; k < range[1]; k++) {
                    subGroup.push(solution[j][k])
                }
            }
            subGroups.push(subGroup)
        }
        return subGroups
    }
    // check each sub-group for dupes and 1-9
    function subCheck(subGroups) {
        for (let group of subGroups) {
            for (let number of group) {
                if (!dupeCheck.includes(number)) {
                    dupeCheck.push(number)
                }
            }
            if (dupeCheck.length < 9) {
                return false
            } else {
                dupeCheck = []
            }
        }
        return true
    }
    // checks each row for dupes, and 1-9
    function rowCheck(row) {
        for (let num of row) {
            if (!dupeCheck.includes(num)) {
                dupeCheck.push(num)
            }
            if (!check.includes(num)) {
                return false
            }
        }
        if (dupeCheck.length < 9) {
            return false
        }
        dupeCheck = []
        return true
    }
  
    // master check
    function masterCheck(solution) {
        if (!subCheck(subGroups)) {
            return false
        } else {
            for (let i = 0; i < solution.length; i++) {
                let r = solution[i]
                if (!rowCheck(r)) {
                    return false
                }
            }
            return true
        }
    } 
    return masterCheck(solution)
}

const validTest = [
    [8,3,5,4,1,6,9,2,7],
    [2,9,6,8,5,7,4,3,1],
    [4,1,7,2,9,3,6,5,8],
    [5,6,9,1,3,4,7,8,2],
    [1,2,3,6,7,8,5,4,9],
    [7,4,8,5,2,9,1,6,3],
    [6,5,2,7,8,1,3,9,4],
    [9,8,1,3,4,5,2,7,6],
    [3,7,4,9,6,2,8,1,5]
]
const invalidTest = [
    [8,3,5,4,1,6,9,2,7],
    [2,9,6,8,5,7,4,3,1],
    [4,1,7,2,9,3,6,5,8],
    [5,6,9,1,1,4,7,8,2],
    [1,2,3,6,7,8,5,4,9],
    [7,4,8,5,2,9,1,6,3],
    [6,5,2,7,8,1,3,3,4],
    [9,8,1,3,4,5,2,7,6],
    [3,7,4,9,6,2,8,1,5]
]
  
console.log(sudokuValidator(validTest))
console.log(sudokuValidator(invalidTest))
  