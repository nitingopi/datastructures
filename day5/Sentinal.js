class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class Sentinal {
    constructor() {
        // const node = new Node(0);
        this.head = new Node(0);
        this.tail = new Node(0);

        //! create sentinal nodes
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    addToBack(value) {

        //! put left and right hands

        const newNode = new Node(value);
        newNode.next = this.tail;
        newNode.prev = this.tail.prev;


        //! pull the new node now 
        newNode.prev.next = newNode;
        newNode.next.prev = newNode;
        return true;

    }

    addToBackValues(...values) { //! Rest arguments
        values.forEach(value => {
            //! put left and right hands
            const newNode = new Node(value);
            newNode.next = this.tail;
            newNode.prev = this.tail.prev;


            //! pull the new node now 
            newNode.prev.next = newNode;
            newNode.next.prev = newNode;
        });
        return true;

    }

    removeValue(searchValue) {

        for (let current = this.head.next; current != this.tail; current = current.next) {
            if (current.value == searchValue) {

                current.prev.next = current.next;
                current.next.prev = current.prev;
                return true;
            }
        }
        return false;

    }

    removeValues(...values) {
        let count = 0;
        // values.forEach(value => {
        //     for (let current = this.head.next; current != this.tail; current = current.next) {
        //         if (current.value == value) {

        //             current.prev.next = current.next;
        //             current.next.prev = current.prev;
        //             count++;
        //             // return true;
        //         }
        //     }
        // });

        //! more efficient way of removing values
        for (let current = this.head.next; current != this.tail; current = current.next) {
            if (values.includes(current.value)) {
                current.prev.next = current.next;
                current.next.prev = current.prev;
                count++;
            }
        }
        return count;
    }

    insertAfter(searchValue, insertValue) {
        //% skip head stop at tail
        for (let current = this.head.next; current != this.tail; current = current.next) {
            if (searchValue == current.value) {
                const newNode = new Node(insertValue);
                newNode.prev = current;
                newNode.next = current.next;
                newNode.prev.next = newNode;
                newNode.next.prev = newNode;
                return true;
            }
        }
        return false;
    }

    insertBefore(searchValue, insertValue) {
        //% skip head stop at tail
        for (let current = this.head.next; current != this.tail; current = current.next) {
            if (searchValue == current.value) {
                const newNode = new Node(insertValue);

                //! climb up the wall 
                newNode.prev = current.prev;
                newNode.next = current;

                //! people on the wall will help you up
                newNode.prev.next = newNode;
                newNode.next.prev = newNode;
                return true;
            }
        }
        return false;
    }

    printForward() {
        let queue = '';
        //! head and tail don't hold any data, so don't include them
        for (let node = this.head.next; node != this.tail; node = node.next) {
            queue += node.value + '-';
        }
        console.log(queue);
    }
}

let sentri = new Sentinal();
//! ADDING VALUES ONE  BY ONE 

// sentri.addToBack(3);
// sentri.addToBack(5);
// sentri.addToBack(7);

//! ADDING VALUES TOGETHER 
sentri.addToBackValues(3, 5, 7);
sentri.printForward();

//! REMOVE VALUES ONE BY ONE
// sentri.removeValue(3);
// sentri.removeValue(7);
// sentri.removeValue(5);
// sentri.removeValue(9)

//! REMOVE VALUES TOGETHER
itemsRemoved = sentri.removeValues(3, 5, 7);
sentri.printForward();
console.log('itemsRemoved ', itemsRemoved);

//! INSERT AFTER ONE BY ONE 
// sentri.insertAfter(3,4);
// sentri.insertAfter(5,6);
// sentri.insertAfter(7,8);
// sentri.printForward();
 
//! INSERT BEFORE ONE BY ONE
// sentri.insertBefore(3,4);
// sentri.insertBefore(5,6);
// sentri.insertBefore(7,8);
// sentri.printForward();






