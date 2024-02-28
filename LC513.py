class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            node_count = len(queue)
            for i in range(node_count):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == 0:
                    ans = node.val

        return ans
