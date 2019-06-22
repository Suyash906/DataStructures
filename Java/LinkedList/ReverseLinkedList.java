class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        if(null == head)
            return head;
        ListNode curr, nextNode;
        curr = head;
        while(curr.next!=null){
            nextNode = curr.next;
            curr.next = nextNode.next;
            nextNode.next = head;
            head = nextNode;
        }
        return head;
    }
}