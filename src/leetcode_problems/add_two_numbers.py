# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def convert_list_to_number(self, input_list):
        final_num = 0
        loop_counter = 0

        while(input_list is not None):
            final_num += (10**loop_counter) * (input_list.val)
            input_list = input_list.next
            loop_counter += 1
    
        return final_num

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result_int = self.convert_list_to_number(l1) + self.convert_list_to_number(l2)
        result_list = list(map(int, str(result_int)[::-1]))
        

        result_head = ListNode(val=result_list[0], next=None)
        result_tail = result_head  

        for num in result_list[1:]:
            temp_node = ListNode(val=num, next=None)
            result_tail.next = temp_node  
            result_tail = temp_node     

            
        return(result_head)