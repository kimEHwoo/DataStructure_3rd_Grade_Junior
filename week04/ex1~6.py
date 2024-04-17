class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# head: 링크드 리스트의 첫 번째 노드를 가리키는 포인터입니다. 함수의 매개변수로 주어진 첫 번째 노드를 나타냅니다.
# dummy: 가상의 노드로, 실제 노드와 연결되는 더미(가짜) 노드입니다. 이 더미 노드는 실제 링크드 리스트의 첫 번째 노드를 가리키며, 이를 통해 삭제 작업을 보다 효율적으로 처리할 수 있습니다.
# prev: 현재 노드의 이전 노드를 가리키는 포인터입니다. 삭제 작업 시 이전 노드의 다음 포인터를 조정하는 데 사용됩니다.
# cur: 현재 탐색 중인 노드를 가리키는 포인터입니다. 링크드 리스트를 탐색하면서 삭제 대상 노드를 확인하기 위해 사용됩니다.

# 이제 removeElements 함수의 동작을 살펴보겠습니다.
# 1. dummy 노드를 생성하고, 이 더미 노드의 next 포인터를 원래 링크드 리스트의 첫 번째 노드(head)로 설정합니다.
# 2. prev와 cur 포인터를 초기화합니다. prev는 가장 처음에는 dummy 노드를 가리키고, cur은 첫 번째 노드를 가리킵니다.
# 3. cur이 끝에 도달할 때까지 반복하는 while 루프를 실행합니다.
# 4. 현재 노드인 cur의 값이 삭제할 값(val)과 일치하는지 확인합니다.
# 5. 만약 일치하면, 이전 노드의 next 포인터를 현재 노드의 다음 노드로 설정하여 현재 노드를 건너뜁니다. 이를 통해 현재 노드가 삭제됩니다.
# 6. 일치하지 않는 경우에는 prev를 cur로 업데이트합니다. 오른쪽으로 한칸씩 옮긴다고 생각
# 7. 마지막으로, 수정된 링크드 리스트의 첫 번째 노드를 반환합니다. 여기서 첫 번째 노드는 dummy 노드의 next 포인터가 가리키는 노드입니다.

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode()
    dummy.next = head
    prev, cur = dummy, head     # prev, cur은 포인터
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next

# linked_list 만들기임
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:      # values[1]부터
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end = " -> ")
        head = head.next
    print("None")

values = [1, 2, 6, 3, 4, 5, 6]
head = create_linked_list(values)
print_linked_list(head)

val = 6

new_head = removeElements(head, val)
print_linked_list(new_head)

# 끝에서 n번째 노드 지우기
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head == None:        # 비어있는 경우
        return head.next    # head.next도 존재하지 않는다.
          
    dummy = ListNode(-1, head)  # dummy : val=-1, dummy.next=head
    fast = dummy.next           # fast = dummy.next, 즉 헤드 노드

    for _ in range(n):      # fast와 slow의 차이는 n
        fast = fast.next    # fast를 헤드 노드를 1번이라하면, n+1번째 노드를 가리킨다.
        slow = dummy        # slow는 dummy 노드, 0번째 노드
    while fast:             
        fast, slow = fast.next, slow.next   # 리스트의 끝에 도달할 때까지 한 칸씩 뒤로 이동
        slow.next = slow.next.next          # slow.next도 한 칸씩 조정
        return dummy.next                   # 헤드 노드
        
values=[1,2,3,4,5,6]
head=create_linked_list(values)
print_linked_list(head)
n=3
new_head=removeNthFromEnd(head,n)
print_linked_list(new_head)