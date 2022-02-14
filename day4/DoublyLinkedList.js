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

    insertAfter(searchValue, value) {
        // let current = this.head;
        // while (current.value != searchValue) {
        //     current = current.next
        // }

        for (let current = this.head; current; current = current.next) {
            if (current.value == searchValue) {
                //* found in tail
                if (current == this.tail) {
                    return (this.addToBack(value), true);
                }
                //* found in middle
                const insertNode = new Node(value);
                insertNode.prev = current; //! left hand on left node
                insertNode.next = current.next; //! right hand on right node
                // current.next.prev = insertNode;  [either this]
                // current.next = insertNode;       [either this]  

                // insertNode.next.prev = insertNode;  // [or this]    
                // insertNode.prev.next = insertNode;  // [or this]

                insertNode.next.prev = insertNode.prev.next = insertNode // [ or only this ]
                return true;

            }
        }

        //value not found [ current = null]
        return false;

    }

    insertBefore(searchValue, value) {
        for (let current = this.tail; current; current = current.prev) {
            if (current.value == searchValue) {
                //! reached head
                if (current == this.head) {
                    return (this.addToFront(value), true);
                }

                //! found in middle
                const insertNode = new Node(value);
                insertNode.next = current;
                insertNode.prev = current.prev;
                insertNode.prev.next = insertNode;
                insertNode.next.prev = insertNode;


                return true;
            }
        }

        //! value not found
        return false;
    }

    removeValue(searchValue) {
        for (let current = this.head; current; current = current.next) {
            //! mil gayiiiii
            if (current.value == searchValue) {
                //% only one node
                if (this.head == this.tail) {
                    this.head = null;
                    this.tail = null;
                    return true;
                }

                //% found in head
                if (current == this.head) {
                    this.head = this.head.next;
                    this.head.prev = null;
                    return true;
                }

                //%found in tail
                if (current == this.tail) {
                    this.tail = this.tail.prev;
                    this.tail.next = null;
                    return true;
                }

                //%found in middle
                current.prev.next = current.next;
                current.next.prev = current.prev;
                return true;
            }

        }
        return false;
    }

    printForward() {
        let current = this.head;
        let queue = '';
        while (current != null) {
            // console.log(current.value)
            queue += current.value + '-';
            current = current.next;
        }
        console.log(queue)
    }

    printBackward() {
        let current = this.tail;
        let queue = '';
        while (current != null) {
            // console.log(current.value);
            queue += current.value + '-';
            current = current.prev;
        }
        console.log(queue);
    }

}

ls = new List();
ls.addToBack(3);
ls.addToBack(4);
ls.addToFront(2);
ls.addToFront(1);
// console.log('Printing forwards');
// ls.printForward();
// console.log('Inserting after');
ls.insertAfter(2, 5);
// console.log('Printing forwards');
// ls.printForward();
// console.log('Printing backwards');
// ls.printBackward();
// console.log('Inserting before');
ls.insertBefore(3, 6);
// console.log('Printing forwards');
ls.printForward();
// console.log('Printing backwards');
// ls.printBackward();
ls.removeValue(5);
ls.printForward();


