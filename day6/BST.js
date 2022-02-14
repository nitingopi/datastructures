class Node {
    constructor(value){
        this.left = null;
        this.value = value;
        this.right = null;
    }
}

class Tree{
    constructor(){
        this.root = null;
    }

    addNode(current, value){ //! recursive function - calling itself
        if(null == current){
            return new Node(value);
        }

        if(value > current.value){
            console.log('before adding right');
            current.right = this.addNode(current.right, value);//! recursion
            console.log('after adding right');
        }else{
            console.log('before  adding left');
            current.left = this.addNode(current.left, value); //! recursion
            console.log('after adding left');
        }
        return current;
    }
    
    //% yeh bhi recursive function hai
    printInOrder(current){  
        if(current){
            this.printInOrder(current.left);
            console.log(current.value);
            this.printInOrder(current.right);
        }
    }

    printPreOrder(current){ 
        if(current){
            console.log(current.value);
            this.printPreOrder(current.left);
            this.printPreOrder(current.right);
        }
    }
    
    printPostOrder(current){ 
        if (current){
            this.printPostOrder(current.left);
            this.printPostOrder(current.right);
            console.log(current.value);
        }

    }
}

const ped = new Tree();
ped.root = ped.addNode(ped.root,5);
ped.addNode(ped.root,7);
ped.addNode(ped.root,9);
ped.addNode(ped.root,-7);
console.log('Printing In Order');
ped.printInOrder(ped.root);
console.log('Printing Pre Order');
ped.printPreOrder(ped.root);
console.log('Printing Post Order');
ped.printPostOrder(ped.root);