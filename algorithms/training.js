class LinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
    };

    append(value){
        const newNode = new Node(value);

        if(!this.head || !this.tail){
            this.head = newNode;
            this.tail = newNode;

            return this;
        };

        if(!this.head){
            this.head = newNode;
        };

        this.tail.next = newNode;
        this.tail = newNode;

        return this;
    };

    extend(value){
        const newNode = new Node(value, this.head);

        this.head = newNode;

        if(!this.tail){
            this.tail = newNode;
        };
    };

    insert(value, prevNode){
        if(prevNode === null){
            return this;
        };

        const newNode = new Node(value, this.head);

        newNode.next = prevNode.next;
        prevNode.next = newNode;

        if(newNode.next === null){
            this.tail = newNode;
        };

        return this;
    };

    find(value){
        if(!this.head){
            return null;
        };

        let curNode = this.head;

        while(curNode){
            if(curNode.value === value){
                return curNode;
            };
            curNode = curNode.next;
        };

        return null;
    };

    len(){
        let curNode = this.head;
        let counter = 0;

        while(curNode){
            counter++;
            curNode = curNode.next;
        };

        return counter;
    };

    delete(value){
        
    };

    toArray(){
        const nodes = [];

        let curNode = this.head;

        while(curNode){
            nodes.push(curNode);
            curNode = curNode.next;
        };

        return nodes;
    };

    toString(){
        return this.toArray().map(node => node.toString()).toString();
    };
};

class Node{
    constructor(value, next = null){
        this.value = value;
        this.next = next
    };

    toString(){
        return `${this.value}`
    };
};

let list = new LinkedList();

list.append(1);
list.extend('a');
list.append("Hello world!");

let prev = list.find('a');
list.insert(2.01, prev);

console.log(list.toString());
console.log(list.len());
console.log(list.find("Hello world!"));