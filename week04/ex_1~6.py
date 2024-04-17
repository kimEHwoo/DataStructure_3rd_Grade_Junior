class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev, cur = dummy, head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next


def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

values = [1, 2, 6, 3, 4, 5, 6]
head = create_linked_list(values)
print_linked_list(head)

val = 6

new_head = removeElements(head, val)
print_linked_list(new_head)



def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head == None:
        return None
    dummy = ListNode(-1, head)

    fast = head
    for _ in range(n-1):
       fast = fast.next
    slow = dummy

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return dummy.next

   
values=[1,2,3,4,5,6]
head=create_linked_list(values)
print_linked_list(head)
n=3
new_head=removeNthFromEnd(head,n)
print_linked_list(new_head)



# 값이 x보다 작은 모든 노드가 x보다 크거나 같은 값의 노드보다 앞에 오도록 하여라.
# 두 파티션의 노드들의 초기 상대적인 순서를 유지해야 한다.

def partition(head: ListNode, x: int) -> ListNode:
    dummy1, dummy2 = ListNode(-1), ListNode(-1)
    p, p1, p2 = head, dummy1, dummy2
    while p:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        temp = p.next
        p.next = None
        p = temp
    p1.next = dummy2.next
    new_node = ListNode(x)
    p1.next = new_node
    p1 = p1.next

    while p1.next:
        p1 = p1.next

    p1.next = dummy2.next
    return dummy1.next

values=[8,9,6,1,4,2,7,10]
head=create_linked_list(values)
print_linked_list(head)
x=5
new_head=partition(head,x)
print_linked_list(new_head)



# 중복된 노드 없애는 함수
# 현재 노드의 값이 이미 visited에 있는지 확인합니다.
# 만약 이미 방문한 값이라면, 이는 중복된 노드이므로 이전 노드 pre의 next를 현재 노드의 next로 설정하여 중복된 노드를 제거합니다.
# 그렇지 않은 경우, 현재 노드의 값을 visited에 추가하고 pre를 현재 노드로 이동시킵니다
def removeDuplicateNodes(head: ListNode) -> ListNode:
        pre, cur = None, head
        visited = set()
        while cur:
            if cur.val in visited:
                pre.next = cur.next
            else:
                visited.add(cur.val)
                pre = cur
            cur = cur.next
        return head

values=[1,2,3,3,2,1]
head=create_linked_list(values)
print_linked_list(head)
new_head=removeDuplicateNodes(head)
print_linked_list(new_head)


# 노드 역순으로 바꾸기
def reverseList(head: ListNode):
    prev, cur = None, head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

values=[1,2,3,4,5]
head=create_linked_list(values)
print_linked_list(head)
new_head=reverseList(head)
print_linked_list(new_head)


# linked list 합치기
def mergeTwoLists(list1:ListNode, list2:ListNode):
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2
        return prehead.next