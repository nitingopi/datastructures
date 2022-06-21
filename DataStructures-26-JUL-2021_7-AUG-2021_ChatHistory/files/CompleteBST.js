
const readline = require("readline-sync");

class Node {
  constructor(value) {
    this.left = null;
    this.value = value;
    this.right = null;
  }
}

class Tree {
  constructor(...values) {
    this._root = null;
    this._level = 0;
    this._count = 0;
    this.add(...values);
  }

  //* Wrapper function for data abstraction, so user can call without giving this.root
  add(...values) {

    values.forEach(value => {

      //! EDIT: Make the internal function inner function, so user cannot call it directly
      function addNode(current, /* value */) {                 //! EDIT We no longer pass value as its in closure above

        //% If we have reached null node, this is where we have to add new node
        if (null == current)
          return new Node(value);

        //% Otherwise, recurse down the tree to find where the new node should be added
        if (value > current.value)
          current.right = addNode(current.right, /*value */);   //! EDIT: functions don't need 'this' to call, value is in closure
        else
          current.left = addNode(current.left, /* value */);    //! EDIT: functions don't need 'this' to call, value is in closure
        return current;
      }

      this._root = addNode(this._root, /* value */);              //! EDIT: functions don't need 'this' to call, value is in closure
    });
    this._count += values.length;
    return values.length;
  }


  //* EDIT: User Wrapper function for data abstraction as outer function
  remove(...values) {
    let countNotRemoved = 0;
    values.forEach(value => {
      //! EDIT: Make the internal function inner function, so user cannot call it directly
      function removeNode(current, /* value */) {               //! EDIT We no longer pass value as its in closure above

        //% We did not find the value to be deleted
        if (null == current) {
          countNotRemoved++;
          return null;
        }

        //% Search the value to be deleted by recursing down the tree
        if (value > current.value)
          current.right = removeNode(current.right, value);     //! EDIT: functions don't need 'this' to call
        else if (value < current.value)
          current.left = removeNode(current.left, value);       //! EDIT: functions don't need 'this' to call
        else {

          //% Found the value to be deleted
          //~ Case 1: Node does not have either left of right
          if (!current.left && !current.right)                  //! EDIT: null == current.left can be !current.left
            return null;  //% Tell parent that node no longer exists

          //~ Case 2: Node has one child, either left or right
          if (!current.left || !current.right)                  //! EDIT: null == current.left can be !current.left
            return current.left ?? current.right; //% Give parent the child

          //~ Case 3: Node has both children, so find successor
          //% Successor is "Left most node of the right subtree"
          let successor = current.right;
          while (successor.left)                                //! EDIT: null != current.left can be just current.left
            successor = successor.left;

          //% Steal the vale of the successor then remove successor itself
          current.value = successor.value;
          value = successor.value;                              //! EDIT: We update the closure value instead of passing
          current.right = removeNode(current.right, /*successor.value*/);
        }
        return current;
      }

      this._root = removeNode(this._root, value);                 //! EDIT: functions don't need 'this' to call
    });
    this._count -= values.length - countNotRemoved;
    return values.length-countNotRemoved;
  }

  //* EDIT: Wrapper function for data abstraction, so user can call without giving root
  print() {
    //! EDIT: It's better to make it arrow function as 'this.level' will fail if it's a function
    const printTree = current => {
      if (current) {

        //% this.level gives us level of the node so we can indent
        this._level++;
        printTree(current.right);

        //% Create leading spaces of level * 4
        console.log(`${" ".repeat(this._level * 4)}${current.value}`);
        printTree(current.left);
        this._level--;
      }
    };

    printTree(this._root);                                       //! EDIT: functions don't need 'this' to call
  }

  //* clear removes all entries from the tree
  clear() {

    //% Easiest in GC languages (JS, Python, Java, C# etc) is to disconnet top node
    //% That would cause all nodes of the tree unreachable and GC will collect them

    this._root = null; //! There goes the entire tree in dustbin
    this._count = 0;
  }

  get length() {
    return this._count;
  }
}

//% main
const ped = new Tree;
let value = 0;

console.log("Simple BST in JavaScript");
while (value = readline.questionInt("Enter a value to insert (0 to stop): ")) {
  ped.add(value);
  console.log(`After adding ${value}, count ${ped.length}`);
  ped.print();
}

while (value = +readline.questionInt("Enter a value to delete (0 to stop): ")) {
  const wasRemoved = ped.remove(value);
  console.log(`${value} was ${wasRemoved ? "removed" : "not removed"}, count ${ped.length}`);
  ped.print();
}

