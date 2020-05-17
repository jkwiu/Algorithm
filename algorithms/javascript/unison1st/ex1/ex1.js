// 다장조는 cdefgabC, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.c는 1로,d는 2로,...C를 8로 바꾼다.1부터 8까지 차례대로 연주한다면 ascending, 8 부터 1 까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다. 연주한 순서가 주어졌을 때, 이것이 ascending 인지, descending 인지, 아니면 mixed 인지 판별하는 프로그램을 작성하시오.
// 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며,1부터 8까지 숫자가 한 번씩 등장한다.
// input: [1,2,3,4,5,6,7,8]
// output: "ascending"

Function.prototype.method = function(name, func){
    if(!this.prototype[name]){
        this.prototype[name] = func;
    }
};

// algorithm
const UnisonAlgorithm = function(){
    this.ex1 = new Ex1();
}

// ex1
const Ex1 = function(){
    this.name = "Ex1";
};

Ex1.method("getSolution", function(arr){

    let ascCnt = 0;
    let descCnt = 0;
    let mixedCnt = 0;
    let rst = "";

    console.log("-----------------------" + this.name + "-----------------------");
    
    for(let i=0; i<arr.length-1; i++){
        if(arr[i+1] == arr[i]+1){   // asc
            ascCnt++;
        } else if(arr[i+1] == arr[i]-1){    // desc
            descCnt++;
        } else {    // mixed
            mixedCnt++;
        }
    }

    if(ascCnt == 7){
        rst = "ascending";
    } else if(descCnt == 7){
        rst = "descending";
    } else {
        rst = "mixed";
    }
    return rst;
});


// create algorithm
const solution = new UnisonAlgorithm();

// ex1
let asc = [1,2,3,4,5,6,7,8];
let desc = [8,7,6,5,4,3,2,1];
let mixed = [8,1,7,2,6,3,5,4];
let test1 = [1,2,3,4,5,6,8,7];
let test2 = [1,8,7,6,5,4,3,2];

let rst1 = solution.ex1.getSolution(asc);
console.log(rst1);

let rst2 = solution.ex1.getSolution(desc);
console.log(rst2);

let rst3 = solution.ex1.getSolution(mixed);
console.log(rst3);

let rst4 = solution.ex1.getSolution(test1);
console.log(rst4);

let rst5 = solution.ex1.getSolution(test2);
console.log(rst5);