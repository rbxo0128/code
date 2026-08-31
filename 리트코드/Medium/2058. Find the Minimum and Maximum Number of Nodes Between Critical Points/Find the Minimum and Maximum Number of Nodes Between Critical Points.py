# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        bb_num = None
        b_num = None

        result = []
        cnt = 0
        min_a = float("inf")
        tmp = None

        while head:
            if not bb_num:
                bb_num = head.val
            elif not b_num:
                b_num = head.val
            else:
                if (b_num > bb_num and b_num > head.val) or (b_num < bb_num and b_num < head.val):
                    if not tmp:
                        tmp = cnt

                    else:
                        min_a = min(min_a, cnt-tmp)
                        tmp = cnt

                    result.append(cnt)

                bb_num = b_num
                b_num = head.val

            head = head.next
            cnt += 1

        if len(result) < 2:
            return [-1,-1]

        return [min_a, result[-1]-result[0]]