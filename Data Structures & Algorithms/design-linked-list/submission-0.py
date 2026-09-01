class MyLinkedList:
    class ListNode:
        def __init__ (self, val=0, prev = None, next = None):
            self.val = val
            self.prev = prev
            self.next = next
    def __init__(self):
        self.left = self.ListNode(0)
        self.right = self.ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.left.next
            while index:
                curr = curr.next
                index -=1
            return curr.val
        

    def addAtHead(self, val: int) -> None:
        new_node = self.ListNode(val)
        new_node.prev = self.left
        new_node.next = self.left.next
        self.left.next.prev = new_node
        self.left.next = new_node
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        new_node = self.ListNode(val)
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev.next = new_node
        self.right.prev = new_node
        self.size +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        else:
            curr = self.left.next
            while index:
                curr = curr.next
                index -= 1
        new_node = self.ListNode(val)
        new_node.next = curr
        new_node.prev = curr.prev
        curr.prev.next = new_node
        curr.prev = new_node
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        else:
            curr = self.left.next
            while index:
                curr = curr.next
                index -= 1
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)