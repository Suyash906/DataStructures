class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        if(null == head || null == head.next)
            return head;
        ListNode p = head;
        ListNode nextNode = null;
        ListNode prev = null;
        while(p != null && p.next!=null){
            nextNode = p.next;
            if(p == head){
                head = nextNode;
            } else {
                prev.next = nextNode;
            }
            p.next = nextNode.next;
            nextNode.next = p;
            prev = p;
            p = p.next;
        }
        return head;
    }
}