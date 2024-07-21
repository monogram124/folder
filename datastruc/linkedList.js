"use strict"

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

        this.tail.next = newNode;

        this.tail = newNode;

        return this;
    };

    toArray(){
        const nodes = [];

        let curNode = this.head;

        while(curNode){
            nodes.push(curNode);
            curNode = curNode.next;
        };
        // знаю
        return nodes;
    };

    toString(){
        return this.toArray().map(node => node.toString()).toString();
    };

    extend(value){
        const newNode = new Node(value, this.head);
        
        this.head = newNode;

        if(!this.tail){
            this.tail = newNode;
        };
        //знаю
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

        //знаю
        return null;
    };

    delete(value){
        if(!this.head){
            return null;
        };

        let delNode = null;

        while(this.head && this.head.value === value){
            delNode = this.head;
            this.head = this.head.next;
        }
 
        let curNode = this.head;

        if(curNode !== null){
            while(curNode.next){
                if(curNode.next.value){
                    delNode = curNode.next;
                    curNode.next = curNode.next.next;
                } else{
                    curNode = curNode.next
                };
            };
        };

        if(this.tail?.value === value){
            this.tail = curNode;
        };

        return delNode;
    };

    insert(value, prevNode){
        if(prevNode === null){
            return this;
        };

        const newNode = new Node(value);

        newNode.next = prevNode.next;
        prevNode.next = newNode;

        if(newNode.next === null){
            this.tail = newNode;
        };

        return this;
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
};

class Node{
    constructor(value, next = null){
        this.value = value;
        this.next = next;
    };

    toString(){
        return `${this.value}`
    };
};

let list = new LinkedList();

list.append(280);
list.append(2.78);
list.extend('a');
list.append(7);
list.extend('Hello world!');

let prev = list.find('a');
list.insert(true, prev);

console.log('Список: ' + list.toString());
console.log('=============');
console.log('Найден элемент: ' + list.find(7));
console.log('Длина списка: ' + list.len());