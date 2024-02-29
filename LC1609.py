from collections import deque

class Solution:
    def isEvenOddTree(self, root):
        dfs = deque()
        dfs.append(root)

        mode = 0
        
        def evenodd():
            nonlocal dfs, mode
            while len(dfs) != 0:
                n = len(dfs)
                mode = abs(mode-1)
                memory = TreeNode(-1) if mode else TreeNode(10**6+2)
                for i in range(n):
                    item = dfs.popleft()
                    if item.val % 2 != mode: return False
                    if item.left: dfs.append(item.left)
                    if item.right: dfs.append(item.right)
                    if mode == 1 and memory.val >= item.val: return False
                    if mode == 0 and memory.val <= item.val: return False
                    memory = item
            return True

        return evenodd()
