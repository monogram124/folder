let counter = 0;
// линейный поиск

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

// console.log(linearSearch(array, 1));
// console.log(counter);

// бинарный поиск (делит массив на двое пока не найдет нужный элемент)

let array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

function binarySearch(array, el){
    
    let start = 0;
    let end = array2.length;
    let middle;
    let found = false;
    let position = -1;

    while(found === false && start <= end){
        counter++;
        middle = Math.floor((start + end) / 2);
        
        if(array[middle] === el){
            found = true;
            position = middle;
            return position;
            
        };

        if(el < array[middle]){
            end = middle - 1;
        } else{
            start = middle + 1;
        };
    };
    return position;
    
};

// console.log(binarySearch(array2, 134));
// console.log(counter);


// сортировка выбором

const array3 = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32];

function selectionSort(array){
    for(let i = 0; i < array.length; i++){
        let indexMin = i;
        for(let j = i+1; j < array.length; j++){
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