let counter = 0;

const array4 = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32];

function bubbleSort(array){
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if(array[j+1] < array[j]){
                let tmp = array[j];
                array[j] = array[j+1]
                array[j+1] = tmp;
            };
            counter++;
        };      
    };
    return array;
};

console.log(bubbleSort(array4));
console.log(counter);

// тренировка
let array = [1, '2'];

console.log(array[1]);