let counter = 0;

let array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

function binarySearch(arr, target){
    let left = 0;
    let right = arr.length - 1
    let mid;

    while(left <= right){
        mid = Math.floor((right-left)/2) + left;

        if(target === arr[mid]){
            return mid
        } else if(target < arr[mid]){
            right = mid + 1
        } else{
            left = mid - 1
        };
    };
    return -1;
};

console.log(binarySearch(array2, 11));
console.log(counter);

// тренировка