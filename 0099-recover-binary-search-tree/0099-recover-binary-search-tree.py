# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def dfs(node) :
            if not node :
                return []

            left_nodes = dfs(node.left)
            right_nodes = dfs(node.right)

            return left_nodes + [node.val] + right_nodes

        nodes = dfs(root)
        number1 , number2 = float('inf') , float('inf')
        
        orderedNodes = sorted(nodes)

        for i in range(len(nodes)) :
            if nodes[i] != orderedNodes[i] :
                number1 , number2 = nodes[i] , orderedNodes[i]


        def traverseTree(node) :
            if not node : 
                return
            
            if node.val == number1 :
                node.val = number2
            elif node.val == number2 :
                node.val = number1

            traverseTree(node.left)
            traverseTree(node.right)

            return


        traverseTree(root)