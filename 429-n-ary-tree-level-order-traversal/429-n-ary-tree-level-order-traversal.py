"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        op = []
        
        while queue:
            ans = []
            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node.val)
                for c in node.children:
                    queue.append(c)
            
            op.append(ans)
            
        return op