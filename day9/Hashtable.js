class Node{
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Hashtable {

    table = [];
    hash(input) {
        return input % this.size;
    }
    constructor(size = 10) {
        this.size = size;
        this.table = new Array(this.size);
    }


    getItem(input) {  //% Search O(1)
        const index = this.hash(input);
        for(let current = this.table[index]; current; current = current.next){
            if (current.value == input){
                return current.value;
            }
        }
        return undefined;
    }
    putItem(input) {  //% Insert O(1)
        const index = this.hash(input);

        const newNode = new Node(input);

        //! collision 
        if(this.table[index]){
            newNode.next = this.table[index]; //! separate chaining
        }
        //! head of linked list 
        this.table[index] = newNode;
    }
    removeItem(input) { //% Delete O(1)
        const index = this.hash(input);

        let back = this.table[index];
        for (let current = this.table[index]; current; current = current.next){
            if (current.value == input){
                if(current == this.table[index]){
                    this.table[index]=current.next;
                    return true;
                }
                back.next = current.next;
                return true;
            }
            back = current;
        }
        return false;

    }

    print() {
        for (let index = 0; index < this.table.length; index++) {
            let str = `${index}: [`
            for (let current = this.table[index]; current; current = current.next){
                str += current.value+", ";
            }
            str += "]";
            console.log(str);
        }
    }

}

const ht = new Hashtable();
ht.putItem(420);
ht.putItem(533);
ht.putItem(224);
ht.putItem(430)
ht.removeItem(2015);
ht.putItem(620);
// ht.removeItem(620);
// ht.removeItem(420);
// ht.removeItem(430);
ht.print();
const isMember = ht.getItem(430);
console.log(`is member ${isMember}`);
