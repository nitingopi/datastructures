class Node {
    constructor(value) {
        this.left = null;
        this.value = value;
        this.right = null;
    }
}

class Tree {
    constructor() {
        this.root = null;
    }

    addNode(current, value) { //! recursive function - calling itself
        if (null == current) {
            return new Node(value);
        }

        if (value > current.value) {
            console.log('before adding right');
            current.right = this.addNode(current.right, value);//! recursion
            console.log('after adding right');
        } else {
            console.log('before  adding left');
            current.left = this.addNode(current.left, value); //! recursion
            console.log('after adding left');
        }
        return current;
    }

    //% yeh bhi recursive function hai
    printInOrder(current) {
        if (current) {
            this.printInOrder(current.left);
            console.log(current.value);
            this.printInOrder(current.right);
        }
    }

    printPreOrder(current) {
        if (current) {
            console.log(current.value);
            this.printPreOrder(current.left);
            this.printPreOrder(current.right);
        }
    }

    printPostOrder(current) {
        if (current) {
            this.printPostOrder(current.left);
            this.printPostOrder(current.right);
            console.log(current.value);
        }

    }

    remove(value) {
        function removeNode(current) {

            if (null == current.value) {
                return null;
            }

            if (value < current.value) {
                current.left = removeNode(current.left) // this will return new child/null to parent
            } else if (value > current.value) {
                current.right = removeNode(current.right) // this will return new child/null to parent
            } else {
                // case 1: node has no children       
                //! current => uda do
                // return null to parent
                if (null == current.left && null == current.right) {
                    return null;
                }

                // case 2: node has left child        
                //! left grand child => child of grandfather
                // return left child to parent
                // if (null != current.left && null == current.right) {
                //     return current.left;
                // }

                // case 3 : node has right child       
                // ! right grand child => child of grandfather
                // return right child to parent
                // if (null != current.right && null == current.left) {
                //     return current.right;
                // }



                // merging case 2 and case 3
                if (null == current.left || null == current.right) {
                    return current.left == null ? current.right  :  current.left;
                }

                //case 4 : node has both children
                // find predecessor or successor
                // predecessor -> right most node of left subtree
                // successor -> left most node of right subtree
                
                let successor = current.right; //! starting point to find successor
                while(successor.left != null){
                    successor = successor.left;
                    console.log(successor.value)
                }
                current.value = successor.value;
                value = successor.value;
                current.right = removeNode(current.right);
            }
            return current;
        }

        this.root = removeNode(this.root);
    }
}

const ped = new Tree();
ped.root = ped.addNode(ped.root, 5);
ped.addNode(ped.root, 7);
ped.addNode(ped.root, 9);
ped.addNode(ped.root, 2);
ped.addNode(ped.root, 3);
ped.addNode(ped.root, 1);
console.log('Printing In Order');
ped.printInOrder(ped.root);
// console.log('Printing Pre Order');
// ped.printPreOrder(ped.root);
// console.log('Printing Post Order');
// ped.printPostOrder(ped.root);
// ped.remove(1);
// ped.remove(3);
// ped.remove(2);
// console.log('Printing In Order');
// ped.printInOrder(ped.root);

ped.remove(2);
console.log('Printing In Order after removing 2 ');
ped.printInOrder(ped.root);
