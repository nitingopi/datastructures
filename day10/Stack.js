class Stack{
    constructor(size=10){
        this.capacity = size;
        this.array = new Array(this.capacity);
        this.top = -1;
    }

    push(value){
        if(this.top == this.capacity-1){
            throw Error('StackOverFlow');
        }
        this.top
    }
}