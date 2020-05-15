import { UnisonAlgorithm } from './common.js';

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

