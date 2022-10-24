# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Time_Complexity: O(n)
#Space_Complexity: O(1)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0    #Initialize lenA as 0
        lenB = 0    #Initialize lenB as 0
        p1 = headA  #Initialize p1 as head1
        p2 = headB  #Initialize p2 as head2
        
        while p1 != None:   #Continue till p1 is not equal to None
            lenA+=1 #Increment lenA by 1 
            p1 = p1.next    #Increment p1 to p1.next
        while p2 != None:   #Continue till p2 is not equal to None
            lenB+= 1    #Increment lenB by 1   
            p2 = p2.next    #Increment p2 to p2.next
         
        p1= headA       #Initialize p1 as headA
        p2 = headB      #Initialize p1 as headB
        while lenA > lenB:  #Continue till lenA is greater than lenB
            p1 = p1.next    #Increment p1 to p1.next
            lenA-=1 #Decerment lenA by 1

        while lenA < lenB:  #Cintune till lenA is less than lenB
            p2 = p2.next    #Increment p2 to p2.next
            lenB-=1     #Decerment lenB by 1
            
        while p1 != p2:     #Continue till p1 is not equal to p2
            p1 = p1.next    #Increment p1 to p1.next
            p2 = p2.next    #Increment p2 to pe.next
            
        return p1   #Return p1 which will give the intersection point in two linked lists
            