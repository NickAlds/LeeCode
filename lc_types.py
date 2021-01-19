from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def print_tree(root):
    if not root:
        return
    print('Binary Tree:')
    print_in_order(root, 0, 'H', 17)


def print_in_order(root, height, preStr, length):
    if not root:
        return
    print_in_order(root.right, height + 1, 'v', length)
    string = preStr + str(root.val) + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string) - leftLen
    res = " " * leftLen + string + " " * rightLen
    print(" " * height * length + res)
    print_in_order(root.left, height + 1, '^', length)


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(-222222222)
    head.right = TreeNode(3)
    head.left.left = TreeNode(523)
    head.right.left = TreeNode(55555555)
    head.right.right = TreeNode(66)
    head.left.left.right = TreeNode(777)
    print_tree(head)
