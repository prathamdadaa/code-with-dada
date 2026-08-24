class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute length and find old tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Calculate effective k
        k = k % length
        if k == 0:
            return head

        # Step 3: Connect tail to head to form a cycle
        tail.next = head

        # Step 4: Find new tail: (length - k - 1)th node from head
        new_tail_steps = length - k - 1
        new_tail = head
        for _ in range(new_tail_steps):
            new_tail = new_tail.next

        # Step 5: Break cycle and assign new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head