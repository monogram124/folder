let counter = 0;

const array = [368,  659,  392, 145, 629, 643,  898,  -57,  127,  746, -191,
    941,  837,  732, 777,  34, 797,  420,  216,  649,  147, -154,
     19,  871,  221, 540, 111, 799,  900,  340,  744,  914,   45,
    520,  897,  363, 928, -20, -30,  717,  299,  553,  749,  465,
    224,  482,  648, 677, 802,   6, -158,  328,  860,  149,  744,
    606,  303,  998, 781,  49,   2,  215,   72,  858,  126,  384,
    968, -127,  732,  27, 811, 391,  922,  136, -176, -154,  801,
   -197,  824,  376, 416, 220, 633,  352, -170,  257,  673,  753,
    -58,  527, -179, 908,  39, 946,  391,  -49,  755, -101, -153,
    654];

function quickSort(array){
    if(array.length <= 1){
        return array;
    };

    let pivotIndex = Math.floor(array.length / 2);
    let pivot = array[pivotIndex];
    let less = [];
    let greater = [];
    
    for(let i = 0; i < array.length; i++){
        counter++;
        
        if(i === pivotIndex){
            continue;
        };
        if(array[i] < pivot){
            less.push(array[i]);
        } else if(array[i] > pivot){
            greater.push(array[i]);
        };
    };
    return [...quickSort(less), pivot, ...quickSort(greater)];
};


// тренировка

console.log(quickSort(array));
console.log(counter);