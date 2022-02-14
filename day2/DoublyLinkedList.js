class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }

}

class List {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToBack(value) {
        const newNode = new Node(value);
        if (null == this.head) {
            this.head = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
        }
        this.tail = newNode;
    }

    addToFront(value) {
        const newNode = new Node(value);
        if (null == this.head) {
            this.tail = newNode;
        } else {
            this.head.prev = newNode;
            newNode.next = this.head;
        }
        this.head = newNode;

    }

    printForward() {
        let current = this.head;
        while (current != null) {
            console.log(current.value)
            current = current.next
        }
    }

    printBackward() {
        let current = this.tail;
        while (current != null) {
            console.log(current.value)
            current = current.prev
        }
    }

}

ls = new List()
ls.addToBack(3)
ls.addToBack(4)
ls.addToFront(2)
ls.addToFront(1)
console.log('Printing backwards');
ls.printForward()
console.log('Printing backwards');
ls.printBackward()