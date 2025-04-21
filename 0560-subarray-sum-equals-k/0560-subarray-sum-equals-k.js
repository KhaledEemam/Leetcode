/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    // let sum = 0
    // let result = 0
    // counter = new Map()
    // counter.set(0,1)

    // for (let num of nums) {
    //     sum += num
    //     const rest = sum - k
        
    //     if (counter.has(rest)) {
    //         result += counter.get(rest)
    //     }

    //     counter.set(sum , (counter.get(sum)||0)+1)
    // }
    // return result
    let sum = 0
    let result = 0
    counter = []
    counter[0] = 1

    for (let num of nums) {
        sum += num
        const rest = sum - k
        
        if (counter[rest] !== undefined) {
            result += counter[rest]
        }

        counter[sum] = (counter[sum] || 0 ) + 1
    }
    return result
};