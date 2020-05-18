// 코이 초등학교에 새로 부임하신 교장 선생님은 어린 학생들의 행복감과 학생들의 성적 차이 관계를 알아보기로 했다. 그래서 이전 성적을 조사하여 학생 들의 시험 점수 차이 변화를 알아보려고 한다.
// 예를 들어서 2016년 학생 8명의 점수가 다음과 같다고 하자. 27, 35, 92, 75, 42, 53, 29, 87
// 그러면 가장 높은 점수는 92점이고 가장 낮은 점수는 27점이므로 점수의 최대 차이는 65이다. 한편 2017년 학생 8명의 점수가 다음과 같았다.
// 85, 42, 79, 95, 37, 11, 72, 32
// 이때 가장 높은 점수는 95점이고 가장 낮은 점수는 11점이므로 점수의 최대 차이는 84이다.
// N 명 학생들의 점수가 주어졌을 때, 가장 높은 점수와 가장 낮은 점수의 차이를 구하는 프로그램을 작성하시오
// 입력
// 표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 학생 수N이 주어진다. 다음 줄에는N명의 학생 점수가 공백 하나를 사이에 두고 주어진다.
// 출력
// 표준 출력으로 가장 높은 점수와 가장 낮은 점수의 차이를 출력한다.

Function.prototype.method = function(name, func){
    if(!this.prototype[name]){
        this.prototype[name] = func;
    }
};

// algorithm
const UnisonAlgorithm = function(){
    this.ex4 = new Ex4();
}

// ex4
const Ex4 = function(){
    this.name = "Ex4";
};

// 순서도. 점수 총합을 출력
// 1. 가장 높은 점수 뽑기
// 2. 가장 낮은 점수 뽑기
// 3. 점수차이 출력
Ex4.method("getSolution", function(gradeArr){
    console.log("-----------------------" + this.name + "-----------------------");
    let topGrade = 0;
    let botGrade = 0;
    // 1. 가장 높은 점수 뽑기
    gradeArr.sort(desc);
    topGrade = gradeArr[0];
    // 2. 가장 낮은 점수 뽑기
    gradeArr.sort(asc);
    botGrade = gradeArr[0];
    // 3. 점수차이 출력
    console.log("가장 높은 점수는: "+topGrade);
    console.log("가장 낮은 점수는: "+botGrade);
    console.log("가장 높은 점수와 가장 낮은 점수의 차이는: ", topGrade-botGrade);
});

// 내림차순
let desc = function(a, b){
    return b-a;
}
// 오름차순
let asc = function(a, b){
    return a-b;
}
// create algorithm
const solution = new UnisonAlgorithm();

let case1 = [27,35,92,75,42,53,29,87];
let case2 = [85,42,79,95,37,11,72,32];
let case3 = [85,42,79,10,37,11,72,100];

solution.ex4.getSolution(case1);
solution.ex4.getSolution(case2);
solution.ex4.getSolution(case3);