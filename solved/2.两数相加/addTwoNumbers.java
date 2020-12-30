import java.util.HashMap;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode cur = head;
        int digit_sum = 0;
        int carry = 0;
        while (l1!=null || l2!=null){
            if (l1!=null && l2!=null){
                digit_sum = l1.val + l2.val + carry;
                l1 = l1.next;
                l2 = l2.next;
            }else if(l1!=null) {
                digit_sum = l1.val + carry;
                l1 = l1.next;
            }else{
                digit_sum = l2.val + carry;
                l2 = l2.next;
            }
            cur.next = new ListNode(digit_sum%10);
            cur = cur.next;
            carry = digit_sum/10;
        }
        if(carry==1){
            cur.next = new ListNode(1);
        }
        return head.next;
    }

}