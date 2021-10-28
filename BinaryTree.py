# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:41:22 2021

@author: Monotera
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
class binaryTree:
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
        
    def level_order():
        pass
    
    def level_order_aux():
        pass
    
    def size():
        pass
    
    def height():
        pass
    
    def size_aux():
        pass
    
    def height_aux():
        pass
    
    
    
                    

    

bt = binaryTree(Node(10))
bt.insert(112)
bt.insert(0)
bt.insert(-1)
bt.insert(2)
bt.insert(3)
bt.pre_order()
bt.pos_order()
bt.in_order()


