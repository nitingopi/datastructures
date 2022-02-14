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

    add(value){
        let ref = new Node(value);
        if (null == this.head ){
            this.head = ref;
            this.tail = ref;
        }else{
            this.tail.next = ref;
            this.tail = ref;    

        }
    }

    print(){
        for (let current = this.head; current; current = current.next){
            console.log(current.value);
        }
    }
}

let ls = new List();
ls.add(1);
ls.add(2);
ls.add(3);
ls.print();