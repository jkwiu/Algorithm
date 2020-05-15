// exporting logics
import { Ex1 } from "./ex1/ex1.js";

Function.prototype.method = function(name, func){
    if(!this.prototype[name]){
        this.prototype[name] = func;
    }
};

// algorithm
const UnisonAlgorithm = function(){
    this.ex1 = new Ex1();
}


export { UnisonAlgorithm };