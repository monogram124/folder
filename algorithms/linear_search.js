let counter = 0;

let array = [1, 2, 35, 2234, 4, 545, 0, 9, 23, 5];

function linearSearch(array, el){
    for(let  i = 0; i < array.length; i++){
        counter ++;
        if(array[i] === el){
            return i;
        };
    };
    return null;
};

console.log(linearSearch(array, 23));
console.log(counter);

// тренировка