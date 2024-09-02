# head = [1,2,3,4,5]
# x=len(head)
# print(x)
# while x > 3:
#     head.pop(0)
#     x=len(head)
    # if x==3:
#         break
#     head.pop(x)
# print(head)
head = [1,2,3,4,5]
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = len(head)
        while x > 3:
            head.pop(0)  
            x = len(head)
            if x == 3:
                break
            head.pop()
            x = len(head)
            print(head)
        return head
