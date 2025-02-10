# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        queue = deque()
        levelToNodes = {}
        queue.append(root)
        levelToNodes[0] = [root.val]
        level_number = 1

        while queue :
            levelNodes = []
            for i in range(len(queue)) :
                node = queue.popleft()

                if node.left :
                    queue.append(node.left)
                    levelNodes.append(node.left.val)
                
                if node.right :
                    queue.append(node.right)
                    levelNodes.append(node.right.val)

            levelToNodes[level_number] = levelNodes
            level_number += 1

        answer = []
        for i in range(len(levelToNodes)-1,-1,-1) :
            if i in levelToNodes  and len(levelToNodes[i]) > 0 :
                answer.append(levelToNodes[i])

        return answer