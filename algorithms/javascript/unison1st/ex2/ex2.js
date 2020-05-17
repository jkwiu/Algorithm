// 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO-FirstInFirstOut- 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
// 1. 현재 Queue 의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
// 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를
// 인쇄하지 않고 Queue 의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
// 예를 들어 Queue에 4개의 문서(ABCD)가 있고, 중요도가 2143 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A,B를 인쇄하게 된다. 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로,A문서는 3번째로 인쇄되게 된다.
// 입력
// 첫 줄에 testcase의 수가 주어진다. 각 testcase에 대해서 문서의 수 N(100이하)와 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue 의 어떤 위치에 있는지를 알려주는
// M(0 이상 N 미만)이 주어진다. 다음줄에 N 개 문서의 중요도가 주어지는데, 중요도는 1 이상 9 이하이다. 중요도가 같은 문서가 여러 개 있을 수도 있다. 위의 예는 N=4,M=0(A문서가 궁금하다면), 중요도는 2143이 된다.
// 출력
// 각 test case 에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

Function.prototype.method = function(name, func){
    if(!this.prototype[name]){
        this.prototype[name] = func;
    }
};

// algorithm
const UnisonAlgorithm = function(){
    this.ex2 = new Ex2();
}

// ex2
const Ex2 = function(){
    this.name = "Ex2";
};

// queue object
const Queue = function(){
    let queue;
}

// 새로운 queue 생성
Queue.method("newQueue", function(name){
    this.queue = [];
});

// queue ele 변경
Queue.method("setQueue", function(i, val){
    this.queue[i] = val;
});

// queue 반환
Queue.method("getQueue", function(name){
    return this.queue;
});

// queue 출력
Queue.method("printQueue", function(){
    console.log(this.queue);
});

// queue에 element 추가
Queue.method("push", function(num){
    this.queue.push(num);
});

// queue에서 element 삭제
Queue.method("pop", function(){
    let arr = [];
    for(let i=1; i<this.queue.length; i++){
        arr[i-1] = this.queue[i];
    }
    this.queue = arr;
});

/**
 * N: 문서의 현재 위치, rst: 해당문서가 출력되는 순서
 */
Ex2.method("getSolution", function(testCase, N){
    console.log("-----------------------" + this.name + "-----------------------");
    if(N > testCase.getQueue().length || N < 0){
        console.log("N을 잘못 입력하셨습니다.");
        return;
    }
    console.log("testcase는 " + testCase.getQueue());
    let rst = 1;
    let arr = [];
    // N번째 배열이 출력되는 순서확인을 위한 배열
    const chkArr = new Queue();
    chkArr.newQueue();
    for(let i=0; i<testCase.getQueue().length; i++){
        arr[i] = testCase.getQueue()[i];
        chkArr.push(testCase.getQueue()[i]);
    }
    chkArr.setQueue(N, "ME");
    let arrIdx = 0;
    let cnt = 0;

    // 순서도가 큰 순서대로 배열 생성
    for(let j=0; j<arr.length; j++){
        for(let i=0; i<arr.length; i++){
            if(i == arr.length){
                break;
            }
            if(arr[i] < arr[i+1]){
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
    }

    // 우선순위대로 출력
    while(testCase.getQueue().length > 0){
        // 가장 큰 우선순위면 출력
        if(testCase.getQueue()[0] == arr[arrIdx]){
            cnt++;
            if(chkArr.getQueue()[0] == "ME"){
                rst = cnt;
            }
            // console.log("출력: " + testCase.getQueue()[0]);
            // console.log(testCase.getQueue());
            // console.log(chkArr.getQueue());
            testCase.pop();
            chkArr.pop();
            arrIdx++;
        } else {    // 아니면 뒤로 보낸다
            testCase.push(testCase.getQueue()[0]);
            chkArr.push(chkArr.getQueue()[0]);
            testCase.pop();
            chkArr.pop();
        }
    }
    
    console.log("문서 인덱스 " + N + "이 출력되는 순서: " + rst);
});

// create algorithm
const solution = new UnisonAlgorithm();

// test case 1
const testCase1 = new Queue();
testCase1.newQueue();
testCase1.push(5);
// testCase1.printQueue();

solution.ex2.getSolution(testCase1, 0);

// test case 2
const testCase2 = new Queue();
testCase2.newQueue();
for(let i=1; i<5; i++){
    testCase2.push(i);
}
// testCase2.printQueue();

solution.ex2.getSolution(testCase2, 2);

// test case 3
const testCase3 = new Queue();
testCase3.newQueue();
testCase3.push(1);
testCase3.push(1);
testCase3.push(9);
testCase3.push(1);
testCase3.push(1);
testCase3.push(1);
// testCase3.printQueue();

solution.ex2.getSolution(testCase3, 0);

// test case 4
const testCase4 = new Queue();
testCase4.newQueue();
testCase4.push(4);
testCase4.push(1);
testCase4.push(3);
testCase4.push(3);
testCase4.push(10);

solution.ex2.getSolution(testCase4, 3);