class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class List {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToBack(value) {
        let ref = new Node(value);
        if (null == this.head) {
            this.head = ref;
        } else {
            this.tail.next = ref;
        }
        this.tail = ref;
    }

    addToFront(value) {
        let ref = new Node(value);
        if (null == this.head) {
            this.tail = ref;
        } else {
            ref.next = this.head;
        }
        this.head = ref;
    }

    print() {
        let queue = '';
        for (let current = this.head; current; current = current.next) {
            queue += current.value + '-';
            // console.log(current.value);
        }
        console.log(queue);
    }

    removeValue(searchValue) {
        let back = this.head;    
        for (let current = this.head; current; current = current.next) {
            if (current.value == searchValue) {
                //! only one node
                if (this.head == this.tail) {
                    this.head = null;
                    this.tail = null;
                }

                //! head case
                if (this.head == current){
                    this.head = current.next;
                    return true;
                }

                //! tail case
                if (this.tail == current){
                    this.tail = back;
                    this.tail.next = null;
                    return true;        
                }

                //! middle case
                back.next = current.next;
                return true;
            }
            back = current;
        }
        return false;
    }
}

let ls = new List();
ls.addToBack(1);
ls.addToBack(2);
ls.addToBack(3);
ls.addToFront(4);
ls.addToFront(5);
ls.print();
ls.removeValue(1);
ls.print();
ls.removeValue(2);
ls.print();
ls.removeValue(3);
ls.print();
ls.removeValue(4);
ls.print();
ls.removeValue(5);
ls.print();