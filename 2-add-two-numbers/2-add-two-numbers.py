# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.makeNumber(l1)
        num2 = self.makeNumber(l2)
        result = num1 + num2
        resultArray = [int(x) for x in str(result)]
        resultArray.reverse()
        
        resultList = curr = ListNode(0)
        
        for i in range(len(resultArray)):
            curr.next = ListNode(resultArray[i])
            curr = curr.next
        
        return resultList.next
        
            
    def getDigit(self, number, jisu):
        return number % (10**jisu)
        
    
    def makeNumber(self, listNode):
        cnt = 0
        num1 = 0
        
        if listNode.next == None:
            return listNode.val
            
        while listNode != None:
            num1 += listNode.val * (10**cnt)
            cnt += 1
            listNode = listNode.next
    
        return num1