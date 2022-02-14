class Node{
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class List{
    constructor(){
        this.head = null;
        this.tail = null;
    }

    addToBack(value){
        let ref = new Node(value);
        if (null == this.head ){
            this.head = ref;
        }else{
            this.tail.next = ref;
        }
        this.tail = ref;
    }

    addToFront(value){
        let ref = new Node(value);
        if (null == this.head ){
            this.tail = ref;
        }else{
            ref.next = this.head;
        }
        this.head = ref;
    }

    print(){
        for (let current = this.head; current; current = current.next){
            console.log(current.value);
        }
    }
}

let ls = new List();
ls.addToBack(1);
ls.addToBack(2);
ls.addToBack(3);
ls.addToFront(4);
ls.addToFront(5);
ls.print(); 