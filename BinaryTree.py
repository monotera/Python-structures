# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:41:22 2021

@author: Monotera

@Theory Taken from: www.geeksforgeeks.org

Binary tree:
    A tree whose elements have at most 2 children is called a binary tree. 
    Since each element in a binary tree can have only 2 children, we typically
    name them the left and right child. Order binary tree is a modification of
    the basic binary tree but the left node is gonna be less than the father node
    and the right node is gonna be greater than the father node.

Example tree:
                    10
                  /   \
                0      112
              /   \
            -1     2
                    \
                     3

TAD Binary:
    insert(data) 
    delete(data):
        -Starting at the root, find the deepest and rightmost node in binary
        tree and node which we want to delete. 
        -Replace the deepest rightmost node’s data with the node to be deleted. 
        -Then delete the deepest rightmost node.
    search(data)
    delete_all()
    pre_order():
        -Tip: use recursion to taverse the tree and print as soon as you enter
        the node
    pre_order_aux(node)
    pos_order():
        -Tip: use recursion to taverse the tree and print as you go back
    pos_order_aux(node)
    in_order():
       -Tip: use recursion to taverse the tree and print as soon as you finish 
       checking all the left nodes
    in_order_aux(node)
    level_order()
        -Create a queue
        -Insert the head in the queue
        -Repeat while there are elements in the queue:
            -Store the first element of the queue in a temp_node
            -Pop the first element
            -print the data from the temp_node
            -if the temp_ node has a left child:
                -Add it to the queue
            -if the temp_node has a right child:
                -Add it to the queue
    size()
    height()

Time complexity:
    Searching: 
        -Worst case O(n)
        -General case O(h) where h is the height
    Insertion:
        -Worst case O(n)
        -General case O(h) where h is the height
    Deletion:
        -Worst case O(n)
        -General case O(h) where h is the height
        
    
    
"""

from collections import deque

class Node:
    
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
class binary_tree:
    def __init__(self,data):
        self.head = data

    def insert(self,data):
        temp_node= self.head
        if(temp_node == None):
            self.head = Node(data)
            return
        while(True):
            if data < temp_node.data:
                if temp_node.left == None:
                    temp_node.left = Node(data)
                    return
                else:
                    temp_node = temp_node.left
            else:
                if temp_node.right == None:
                    temp_node.right = Node(data)
                    return
                else:
                    temp_node = temp_node.right
                    
    def delete():
        pass
    
    def search():
        pass
    
    def delete_all():
        pass
    
    def pre_order(self):
        self.pre_order_aux(self.head)
        print("")
    
    def pre_order_aux(self,node):
        print(node.data, end=" -> ")
        if node.left != None:
            self.pre_order_aux(node.left)
        if node.right != None:
            self.pre_order_aux(node.right)
   
    def in_order(self):
        self.in_order_aux(self.head)
        print("")
    
    def in_order_aux(self,node):
        if node.left != None:
            self.in_order_aux(node.left)
        print(node.data, end=" -> ")
        if node.right != None:
            self.in_order_aux(node.right)
            
    def pos_order(self):
        self.pos_order_aux(self.head)
        print("")
    
    def pos_order_aux(self,node):
        if node.left != None:
            self.pos_order_aux(node.left)
        if node.right != None:
            self.pos_order_aux(node.right)
        print(node.data, end=" -> ")

    def level_order(self):
        q = deque()
        q.append(self.head)
        while q:
            temp_node = q[0]
            q.popleft()
            print(temp_node.data, end=" -> ")
            if temp_node.left != None:
                q.append(temp_node.left)
            if temp_node.right != None:
                q.append(temp_node.right)
        print("")
        
    
    def size():
        pass
    
    def height():
        pass
    
    def size_aux():
        pass
    
    def height_aux():
        pass
    
    
    
                    

    

bt = binary_tree(Node(10))
bt.insert(112)
bt.insert(0)
bt.insert(-1)
bt.insert(2)
bt.insert(3)
print("Pre-order")
bt.pre_order()
print("Pos-order")
bt.pos_order()
print("In-order")
bt.in_order()
print("Level-order")
bt.level_order()


