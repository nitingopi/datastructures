// class Node{
//     constructor(value) {
//         this.value = value;
//         this.next = null;
//     }
// }

class Hashtable2 {

    table = [];
    hash(key) {
        return key % this.size;
    }
    constructor(size = 10) {
        this.size = size;
        this.table = new Array(this.size);
    }


    getItem(key) {  //% Search O(1)
        const offset = this.hash(key);

        for (let current = this.table[offset]; current; current = current.next) {
            if (current.key == key) {
                return current;
            }
        }
        return undefined;

    }
    putItem(key, value) {  //% Insert O(1
        const offset = this.hash(key);
        for (let current = this.table[offset]; current; current = current.next) {
            //! scenario 1 : key already exists
            if (key == current.key) {
                current.value = value;
                return false;
            }
        }
        //! scenario 2: key key does not exist
        const newEntry = { key, value }
        newEntry.next = this.table[offset];
        this.table[offset] = newEntry;
    }
    removeItem(key) { //% Delete O(1)
        const offset = this.hash(key);
        let back = this.table[offset];

        for (let current = this.table[offset]; current; current = current.next) {
            if (key == current.key) {

                //% check if it's first node
                if (current == this.table[offset]) {

                    this.table[offset] = this.table[offset].next; //* fly over first node    
                    return true;
                }

                //% if it's not first node - back, do your magic    

                back.next = current.next;
                return true;
            }
            back = current;
        }
        return false;


    }

    print() {
        for (let index = 0; index < this.table.length; index++) {
            let str = `${index}: {`
            for (let current = this.table[index]; current; current = current.next) {
                str += `{${current.key}:${current.value}}` + (current.next ? ", " : "");
            }
            str += "}";
            console.log(str);
        }
    }

}

const ht2 = new Hashtable2();
ht2.putItem(420, "smallB");
ht2.putItem(533, "queenB");
ht2.putItem(224, "momB");
ht2.putItem(430, "bayB")
ht2.removeItem(2015);
ht2.putItem(620, "hayB");
// ht.removeItem(620);
// ht.removeItem(420);
// ht.removeItem(430);
ht2.print();
const isMember = ht2.getItem(430);
console.log(`is member ${isMember}`);
ht2.removeItem(430);
ht2.print();
