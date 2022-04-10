class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_int(node):
 i=0
 result=0
 print("got in")
 while(node!=None):
  print("interation :",i)
  result+=node.val*10**i
  i+=1
  node=node.next
 return result
def tolist(n):
    node = ListNode(n % 10)
    if n > 9:
        node.next = tolist(n // 10)
    return node
   

n13=ListNode(4,None)
n12=ListNode(6,n13)
n11=ListNode(5,n12)

print("making it int ...")
print(make_int(n11))

L=tolist(make_int(n11))
print("making it list ...")
while(L!=None):
 print(L.val)
 L=L.next