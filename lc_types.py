from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def construct_linked_list(l):
    dummy = cur = ListNode()
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next


def print_linked_list(head):
    print("[",end='')
    while head:
        print(head.val, end=', ')
        head = head.next
    print("]")


if __name__ == '__main__':
    l = construct_linked_list([1,2])
    print_linked_list(l)
