from typing import Optional, Tuple

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:

    def insert_node_at_tail(self, head: Optional[Node], x: int) -> Node:
        temp = Node(x)

        if head is None:
            return temp

        cur = head
        while cur.next is not None:
            cur = cur.next

        cur.next = temp

        return head

    def insert_node_at_head(self, head: Optional[Node], x: int) -> Node:
        temp = Node(x)

        temp.next = head
        head = temp

        return head

    def insert_cycle(self, head: Optional[Node], pos: int) -> Optional[Node]:
        prev = head 
        cur = head
        curx = None
        counter = 0

        while cur:

            if (counter == pos):
                curx = cur
            prev = cur
            cur = cur.next
            counter += 1

        prev.next = curx
        return head

    def length(self, head: Optional[Node]) -> int:
        len = 0

        while head:
            len += 1
            head = head.next

        return len

    def create_intersection(self, headA: Node, headB: Node, headC: Node) -> Tuple:
        cur_A = headA
        cur_B = headB

        while cur_A.next is not None:
            cur_A = cur_A.next

        while cur_B.next is not None:
            cur_B = cur_B.next

        cur_A.next = headC
        cur_B.next = headC

        return headA, headB

    def display(self, head: Optional[Node]) -> None:
        if head is None:
            print('List is empty')
            return

        while head is not None:
            print(head.val, end=' ')
            head = head.next