def mergeSortedList(head1,head2):
	if None == head1 and None == head2 :
		return None
	if None == head1:
		return head2
	if None == head2:
		return head1

	while head1 != None and head2!= None:
		if head1.data < head2.data:
			res.data = head1.data
			head1 = head1.next
		else:
			res.data = head2.data
			head2 = head2.next
		res = res.next

	while head1 != None:
		res.data = head1.data
		head1 = head1.next
		res = res.next

	while head2 != None:
		res.data = head2.data
		head2 = head2.next
		res = res.next

	return res