from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    # def __str__(self):
    #     return f'Node:{self.value}'

    # def __repr__(self):
    #     return f'Node:{self.value}'

def tree_by_levels(node):
    if node:
        que = deque([node])
        curr = node
        result = [curr.value]
        while curr:
            if curr.left:
                result.append(curr.left.value)
                que.append(curr.left)
            if curr.right:
                result.append(curr.right.value)
                que.append(curr.right)
            if curr == node:
                que.popleft()
            if que:
                curr = que.popleft()
            else:
                break
        return result
    else:
        return []
