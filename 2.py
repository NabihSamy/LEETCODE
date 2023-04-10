# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            while node.next is not None:
                print(node.val)
                number = node.val
                number =+ node.val *10
                node = node.next 
            return number
        def tolist(number):
            first = node = ListNode(number%10)
            number = number / 10
            while number > 9:   
                node = node.next = ListNode(number%10)
                number = number / 10
                print(number)
            return node
        return tolist(toint(l1)+toint(l2))

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print(result)

        