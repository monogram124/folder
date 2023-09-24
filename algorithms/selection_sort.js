let counter = 0;

const array3 = ['a', 'c', 's', 'd'];

function selectionSort(array){
    for(let i = 0; i < array.length; i++){
        for(let j = i+1; j < array.length; j++){
        let indexMin = i;
            if(array[j] < array[indexMin]){
                indexMin = j;
            };
            counter++;
        };
        let tmp = array[i];
        array[i] = array[indexMin];
        array[indexMin] = tmp;
    };
    return array;
};

console.log(selectionSort(array3));
console.log(counter);