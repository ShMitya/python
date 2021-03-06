
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
    
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
            
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)                
            node = node.next
        return node_list
    
    def delete(self, val, all=False):
        initial_head = self.head
        node = self.head
        
        # особое правило для головы:
        if node is not None and node.value == val:
            if all == True:
                while node is not None and node.value == val:
                    if self.head.next == None:
                        self.head = None
                        self.tail = None
                    elif self.head.next.next == None:
                        self.head = self.tail
                    else:
                        self.head = node.next
                    node = node.next
            elif all == False:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                elif self.head.next.next == None:
                    self.head = self.tail
                else:
                    self.head = node.next
                    
        
            # для остальных узлов:
        while node and node.next is not None:
            if node.next.value == val and initial_head.value !=val and  all == False:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                else:
                    node.next = node.next.next
                return
            elif all == True: 
                while node and node.next is not None and node.next.value == val:
                    if node.next.next == None:
                        node.next = None
                        self.tail = node
                    else:
                        node.next = node.next.next
            node = node.next
        pass
    
    def clean (self):
        self.head= None
        self.tail= None
        pass
        
    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node=node.next
        return i
    
    def insert(self, afterNode, newNode):
        if self.head is None and afterNode == None:
            self.head = newNode
            self.tail = self.head
               
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode_next = node.next
                node.next = newNode
                node.next.next = newNode_next
                if node.next.next == None:
                    self.tail = node.next                    
                return
            node = node.next
