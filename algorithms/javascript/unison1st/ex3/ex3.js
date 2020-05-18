// 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다. 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
// 입력
// 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N 이 주어진다. 이 값은 1,000 보다 작거나 같은 자연수이다. 둘째부터 N 개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는
// 50 보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
// 출력
// 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

Function.prototype.method = function(name, func){
    if(!this.prototype[name]){
        this.prototype[name] = func;
    }
};

// algorithm
const UnisonAlgorithm = function(){
    this.ex3 = new Ex3();
}

// ex3
const Ex3 = function(){
    this.name = "Ex3";
};

// 순서도
// 1. 팔린 책을 count
// 2. 많이 팔린 책을 뽑는다.
// 3. 가장 많이 팔린 책의 숫자 중복된다면 알파벳 순 정렬
// 4. 가장 많이 팔린 책 출력
// input: N(배열의 길이), name(책이름)
Ex3.method("getSolution", function(N, nameArr){
    console.log("-----------------------" + this.name + "-----------------------");
    let soldBookObj = {};
    let length = N;
    let bestSellerCnt = 0;
    let bestSellerArr = [];

    // 1. 팔린 책을 count
    for(let i=0; i<length; i++){
        if(soldBookObj[nameArr[i]] != null){
            soldBookObj[nameArr[i]]++;
        } else {
            soldBookObj[nameArr[i]] = 1;
        }
    }

    // 2. 많이 팔린 책을 뽑는다.
    for(i in soldBookObj){
        if(soldBookObj[i] > bestSellerCnt){
            bestSellerCnt = soldBookObj[i];
        }
    }
    for(i in soldBookObj){
        if(soldBookObj[i] == bestSellerCnt){
            bestSellerArr.push(i);
        }
    }

    // 3. 가장 많이 팔린 책의 숫자 중복된다면 알파벳 순 정렬
    if(bestSellerArr.length > 1){
        bestSellerArr.sort();
    }


    // 4. 가장 많이 팔린 책 출력
    console.log("가장 많이 팔린 책은: ");
    for(i in bestSellerArr){
        console.log(bestSellerArr[i]); 
    }
});

// create algorithm
const solution = new UnisonAlgorithm();

let N1 = 5;
let test1 = ['top', 'top', 'top', 'top', 'kimtop'];

let N2 = 12;
let test2 = ['top', 'top', 'top', 'top', 'kimtop', 'kimtop', 'kimtop', 'kimtop', 'aimtop', 'aimtop', 'aimtop', 'aimtop'];

let N3 = 8;
let test3 = ['a', 'b', 'c', 'c', 'b', 'b', 'a', 'a'];

solution.ex3.getSolution(N1, test1);
solution.ex3.getSolution(N2, test2);
solution.ex3.getSolution(N3, test3);
