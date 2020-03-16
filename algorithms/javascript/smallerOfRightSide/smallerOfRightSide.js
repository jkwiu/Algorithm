const input = [5,2,6,1];

var solution = function(arr){
    let Count = 0;
    for(let i=0; i<arr.length; i++){
        for(let j=i+1; j<arr.length; j++){
            if(arr[i] > arr[j]){
                Count++;
            }
        }
        console.log(Count);
        Count = 0;
    }
}

solution(input);