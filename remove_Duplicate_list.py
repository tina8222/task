class listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def removeduplicate(head):
    node = head
    
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    
    return head

def print_list(gere):
    vals = []
    while gere:
        










            
            
result = removeduplicate(n1)


cur = result

while cur:
    print(cur.val,end=" ")
    cur = cur.next
            