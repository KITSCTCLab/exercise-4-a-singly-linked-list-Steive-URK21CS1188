from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next

class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode  
            
    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            for i in self.next:
                print(self.data)

class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        third_list=LinkedList()
        f=Optional[first_list]
        s=Optional[second_list]
        s=""
        s1=""
        for i in f:
            s=str(i)+s
        for j in s:
            s1=str(j)+s1
        a=int(s)
        b=int(s1)
        c=a+b
        third_list.insert_at_end(c)
        return third_list
        
        head = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:
            s= carry
            if l1 is not None:
                s+= l1.val
                l1 = l1.next
            if l2 is not None:
                s+= l2.val
                l2 = l2.next
            node = ListNode(sum_valu% 10)
            carry = s// 10
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        return head
    
# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
