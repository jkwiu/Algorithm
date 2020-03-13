// Given two arrays, write a function to compute their intersection.

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Note:

// Each element in the result must be unique.
// The result can be in any order.

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const rst = [];
    // memoization 기법으로 중복 계산을 막는다.
    const cache = {};
    for(i in nums1){
        for(j in nums2){
            // arr1과 arr2의 값에 intersection이 존재할 시
            if(nums1[i] === nums2[j]){
                // 캐시에 저장되어있으면 스킵
                if(typeof(cache[nums1[i]]) === 'number'){
                    continue;
                } else {
                    // 없던 값이면 rst arr에 푸쉬하고, 결과 값을 캐시에 기록
                    rst.push(nums1[i]);
                    cache[nums1[i]] = 1;
                }
            }
        }
    }
    console.log(rst);
    return rst; //output: 160ms, 40mb
};

var arr1 = [1,2,3,4,5];
var arr2 = [5,5,5];
// intersection(arr1, arr2);


var intersection2 = function(l1, l2) {
    l1.sort((a, b) => a - b) // assume sorted
    l2.sort((a, b) => a - b) // assume sorted
    const intersections = []
    let l = 0, r = 0;
    while ((l2[l] && l1[r]) !== undefined) {
        const left = l1[r], right = l2[l];
        if (right === left) {
            intersections.push(right)
            while (left === l1[r]) r++;
            while (right === l2[l]) l++;
            continue;
        }
        if (right > left) while (left === l1[r]) r++;
        else while (right === l2[l]) l++;
        
    }
    return intersections; //output: 60ms, 30mb
 };
console.log(intersection2(arr1, arr2));
 