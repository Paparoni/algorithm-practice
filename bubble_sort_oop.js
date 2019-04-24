'use strict'
let myArr = [28, 6, 5, 42, 20, 12, 2, 48, 3, 33, 31, 44, 1, 22, 25, 13, 16, 39, 37, 49, 4, 35, 10, 14, 26, 38, 24];
Array.prototype.swap = function(i, j){
  let temp = this[j]
  this[j] = this[i]
  this[i] = temp
  
}
Array.prototype.bubble_sort = function() {
  for(let k = 0; k < this.length; k++) {
    for(let j = 0; j < this.length - k; j++){
      if(this[j] > this[j + 1]){
        this.swap(j, j+1)
      }
    }
  }
  return this;
  
}
console.log(myArr.bubble_sort())
