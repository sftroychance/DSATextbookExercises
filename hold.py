# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Peter
def remove_nth_from_end(arr, n):
        if head.next == None:
            return None

        end = head
        while n >= 0 and end:
            end = end.next
            n -= 1
        if end == None and n > 0:
            return head
        begin = head

        while end:
            end = end.next
            begin = begin.next
        if begin == head or begin.next == None:
            begin.next = None
        else:
            begin.next = begin.next.next
        return head

# troy
def remove_nth_from_end(arr, n):
    dummy = ListNode('dummy')
    dummy.next = head

    left = dummy

    right = head
    right_position = 1

    while right:
        right = right.next
        right_position += 1

        if right_position > n + 1:
            left = left.next

    left.next = left.next.next

    return dummy.next

# ben
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = ListNode(False, head)
        current = head
        follow = dummy

        counter = 0
        while current.next:
            current = current.next
            counter += 1
            if counter < n:
                continue
            follow = follow.next

        temp = follow.next.next if follow.next else None
        if follow.next:
            follow.next.next = None
        follow.next = temp
        return dummy.next


# Chris
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        snip_start, curr = head, head
        count = 0
        while curr:
            if count == n:
                if not curr.next:
                    snip_start.next = curr
                    return dummy.next

                snip_start = snip_start.next
                count -= 1

            count += 1
            curr = curr.next

        return dummy.next

# My attempt this time was to try to keep a lagging pointer that doesn't start  moving until we're on our nth iteration. It doesn't work for small arrays, though, and I don't want to hack together multiple case-specific guard clauses.

# Reference solution

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while n > 0 and curr:
            curr = curr.next
            n -=1

        while curr:
            prev, curr = prev.next, curr.next

        prev.next = prev.next.next

        return dummy.next

