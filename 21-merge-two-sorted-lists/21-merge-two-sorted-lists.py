# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = first = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                #print(Next.val)
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                #print(Next.val)
                list2, cur = list2.next, list2
        
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        
        return first.next
    
        '''
        if list1.next:
            result.next = list1
        else:
            result.next = list2
        '''